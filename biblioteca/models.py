from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Autor(models.Model):
    """Modelo para representar un autor de libros"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Autores"
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    """Modelo para categorías de libros"""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    """Modelo para editoriales de libros"""
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=50, blank=True)
    sitio_web = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Editoriales"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    """Modelo principal para representar libros"""
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('mantenimiento', 'En Mantenimiento'),
        ('perdido', 'Perdido'),
    ]
    
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, help_text='ISBN de 13 dígitos')
    autores = models.ManyToManyField(Autor, related_name='libros')
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    numero_paginas = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    idioma = models.CharField(max_length=50, default='Español')
    descripcion = models.TextField(blank=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['titulo']
        verbose_name_plural = "Libros"
    
    def __str__(self):
        return self.titulo
    
    def esta_disponible(self):
        """Verifica si el libro está disponible para préstamo"""
        return self.estado == 'disponible'
    
    def autores_str(self):
        """Retorna los autores como string"""
        return ", ".join([autor.nombre_completo() for autor in self.autores.all()])


class Prestamo(models.Model):
    """Modelo para gestionar préstamos de libros"""
    
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('devuelto', 'Devuelto'),
        ('atrasado', 'Atrasado'),
    ]
    
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_estimada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    observaciones = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-fecha_prestamo']
        verbose_name_plural = "Préstamos"
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username} ({self.fecha_prestamo})"
    
    def esta_atrasado(self):
        """Verifica si el préstamo está atrasado"""
        if self.estado == 'devuelto':
            return False
        return timezone.now().date() > self.fecha_devolucion_estimada
    
    def dias_restantes(self):
        """Calcula los días restantes para la devolución"""
        if self.estado == 'devuelto':
            return 0
        diferencia = self.fecha_devolucion_estimada - timezone.now().date()
        return diferencia.days
    
    def save(self, *args, **kwargs):
        """Override del método save para actualizar el estado del libro"""
        # Si es un nuevo préstamo
        if not self.pk:
            self.libro.estado = 'prestado'
            self.libro.save()
        
        # Verificar si está atrasado
        if self.esta_atrasado() and self.estado == 'activo':
            self.estado = 'atrasado'
        
        # Si se devuelve el libro
        if self.fecha_devolucion_real:
            self.estado = 'devuelto'
            self.libro.estado = 'disponible'
            self.libro.save()
        
        super().save(*args, **kwargs)


class Perfil(models.Model):
    """Modelo para extender la información del usuario"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    libros_prestados_max = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Número máximo de libros que puede tener prestados simultáneamente'
    )
    
    class Meta:
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    def prestamos_activos(self):
        """Retorna el número de préstamos activos"""
        return self.usuario.prestamos.filter(estado__in=['activo', 'atrasado']).count()
    
    def puede_pedir_prestamo(self):
        """Verifica si el usuario puede pedir más libros prestados"""
        return self.prestamos_activos() < self.libros_prestados_max
