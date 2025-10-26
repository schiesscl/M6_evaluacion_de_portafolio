from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Category(models.Model):
    """Modelo de categoría de productos"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """Modelo de producto"""
    name = models.CharField(max_length=200, verbose_name='Nombre del Producto')
    description = models.TextField(verbose_name='Descripción')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='products',
        verbose_name='Categoría'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Precio'
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name='Stock'
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name='Imagen'
    )
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products_created',
        verbose_name='Creado por'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        """Verifica si hay stock disponible"""
        return self.stock > 0
    
    @property
    def stock_status(self):
        """Retorna el estado del stock"""
        if self.stock == 0:
            return 'Sin stock'
        elif self.stock < 10:
            return 'Stock bajo'
        else:
            return 'Disponible'
