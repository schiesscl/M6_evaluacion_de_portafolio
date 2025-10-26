# Evaluación de Portafolio Bootcamp Fullstack Python - Módulo 6
## Hans Schiess
### Sistema de Gestión de Productos - Django

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema web completo de gestión de productos desarrollado con Django 5.2.7, implementando las mejores prácticas de desarrollo web empresarial.

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características de Django](#-características-de-django)
- [Comparativa con Otros Frameworks](#-comparativa-con-otros-frameworks)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades Implementadas](#-funcionalidades-implementadas)
- [Panel de Administración](#-panel-de-administración)
- [Requerimientos Cumplidos](#-requerimientos-cumplidos)
- [Contribución](#-contribución)
- [Autor](#-autor)

---

## 📖 Descripción

Este proyecto es una aplicación web empresarial desarrollada como parte del portafolio del **Módulo 6 - Talento Digital**. Implementa un sistema completo de gestión de productos con autenticación de usuarios, panel administrativo y operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

### 🎯 Objetivo

Demostrar el dominio de Django como framework web de alto nivel, implementando:
- Sistema de autenticación y autorización
- Gestión de base de datos con ORM
- Templates dinámicos con Bootstrap
- Formularios con validación
- Panel de administración personalizado
- Arquitectura MVT (Model-View-Template)

---

## 🌟 Características de Django

Django es un framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático. Fue diseñado para ayudar a los desarrolladores a llevar las aplicaciones desde el concepto hasta la finalización lo más rápido posible.

### Ventajas de Django para Aplicaciones Empresariales

#### 1. **Desarrollo Rápido**
- Sistema de plantillas eficiente
- ORM integrado que elimina la necesidad de escribir SQL
- Panel de administración automático
- Sistema de formularios robusto
- **Tiempo de desarrollo:** Hasta 40% más rápido que frameworks tradicionales

#### 2. **Seguridad Incorporada**
- ✅ Protección contra **SQL Injection**
- ✅ Protección contra **Cross-Site Scripting (XSS)**
- ✅ Protección contra **Cross-Site Request Forgery (CSRF)**
- ✅ Protección contra **Clickjacking**
- ✅ Sistema de autenticación robusto
- ✅ Hasheo seguro de contraseñas (PBKDF2, bcrypt, Argon2)

#### 3. **Escalabilidad**
- Arquitectura modular (apps reutilizables)
- Soporte para múltiples bases de datos
- Sistema de caché integrado
- Optimización de consultas (select_related, prefetch_related)
- Manejo eficiente de archivos estáticos

#### 4. **ORM Potente**
- Mapeo objeto-relacional intuitivo
- Consultas complejas sin SQL
- Migraciones automáticas
- Soporte para múltiples bases de datos

#### 5. **Ecosistema Rico**
- Más de 4,000 paquetes en PyPI
- Comunidad activa y grande
- Documentación exhaustiva
- Django REST Framework para APIs

#### 6. **Administración Automática**
- Panel de administración listo para usar
- Altamente personalizable
- Gestión de usuarios y permisos
- CRUD automático para modelos

---

## ⚖️ Comparativa con Otros Frameworks

### Django vs Flask vs FastAPI

| Característica | Django | Flask | FastAPI |
|----------------|--------|-------|---------|
| **Tipo** | Full-stack Framework | Microframework | API Framework |
| **Filosofía** | "Batteries included" | Minimalista | Moderno y rápido |
| **Curva de Aprendizaje** | Media-Alta | Baja | Media |
| **ORM Incluido** | ✅ Django ORM | ❌ Requiere SQLAlchemy | ❌ Compatible con varios |
| **Admin Panel** | ✅ Automático | ❌ Requiere Flask-Admin | ❌ No incluido |
| **Sistema de Templates** | ✅ Django Templates | ✅ Jinja2 | ❌ Frontend separado |
| **Autenticación** | ✅ Integrada | ⚠️ Requiere extensiones | ⚠️ JWT manual |
| **Formularios** | ✅ Django Forms | ⚠️ WTForms | ❌ Frontend |
| **Validación** | ✅ Integrada | ⚠️ Manual | ✅ Pydantic |
| **Seguridad** | ✅ CSRF, XSS, SQL Injection | ⚠️ Configuración manual | ⚠️ Configuración manual |
| **Async Support** | ✅ Desde 3.1 | ✅ Nativo | ✅ Nativo |
| **Rendimiento** | Bueno | Muy Bueno | Excelente |
| **Tamaño Proyecto** | Grande/Mediano | Pequeño/Mediano | APIs/Microservicios |
| **Migración BD** | ✅ Automática | ❌ Alembic manual | ❌ Alembic/Manual |
| **Documentación** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Comunidad** | Muy Grande | Grande | Creciente |
| **Casos de Uso** | Aplicaciones empresariales completas, CMS, e-commerce | Proyectos pequeños, APIs simples, prototipos | APIs REST modernas, microservicios, aplicaciones ML |

### 🏆 ¿Cuándo usar cada uno?

#### Usa **Django** cuando:
- ✅ Necesitas una aplicación web completa (frontend + backend)
- ✅ Requieres panel de administración
- ✅ Trabajas con bases de datos relacionales complejas
- ✅ Necesitas seguridad robusta desde el inicio
- ✅ Quieres desarrollo rápido con menos decisiones
- ✅ Proyectos empresariales de mediano a gran tamaño

**Ejemplos:** Instagram, Pinterest, Mozilla, The Washington Post, National Geographic

#### Usa **Flask** cuando:
- ✅ Necesitas máxima flexibilidad
- ✅ Proyecto pequeño o prototipo rápido
- ✅ API simple sin muchas funcionalidades
- ✅ Quieres elegir tus propias bibliotecas
- ✅ Microservicios ligeros

**Ejemplos:** LinkedIn (partes), Netflix (herramientas internas), Reddit (inicialmente)

#### Usa **FastAPI** cuando:
- ✅ Construyes APIs REST modernas
- ✅ Necesitas alto rendimiento
- ✅ Trabajas con tipos de datos (type hints)
- ✅ Requieres documentación automática (Swagger/OpenAPI)
- ✅ Aplicaciones de Machine Learning/Data Science
- ✅ Microservicios asíncronos

**Ejemplos:** Uber, Microsoft, Netflix (microservicios)

### 📊 Matriz de Decisión

```
                    Complejidad del Proyecto
                    │
    Alto Rendimiento│     FastAPI    │    Django
                    │                │
                    │ ───────────────┼──────────────
                    │                │
    Flexibilidad    │     Flask      │    Django
                    │                │
                    └────────────────┴──────────────
                         Simple          Complejo
```

### 💡 Conclusión

**Django fue elegido para este proyecto porque:**

1. ✅ Proporciona todo lo necesario para una aplicación web completa
2. ✅ Panel de administración automático ahorra desarrollo
3. ✅ Seguridad robusta sin configuración adicional
4. ✅ ORM potente para gestión de base de datos
5. ✅ Sistema de formularios con validación integrada
6. ✅ Ideal para aplicaciones empresariales escalables
7. ✅ Documentación exhaustiva y comunidad activa

> 📖 **Para un análisis más detallado de las diferencias entre frameworks, consulta:** [FRAMEWORKS_COMPARISON.md](FRAMEWORKS_COMPARISON.md)

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python** 3.x
- **Django** 5.2.7
- **SQLite3** (Base de datos)
- **Pillow** 12.0.0 (Procesamiento de imágenes)

### Frontend
- **Bootstrap** 5.3.2
- **Bootstrap Icons** 1.11.3
- **HTML5**
- **CSS3**
- **JavaScript** (Bootstrap Bundle)

### Herramientas de Desarrollo
- **Git** & **GitHub** (Control de versiones)
- **VS Code** (Editor)
- **Python Virtual Environment**

---

## 📦 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git
- Navegador web moderno

---

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/HansSchiess/Evaluacion_portafolio_6.git
cd Evaluacion_portafolio_6
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Contenido de requirements.txt:**
```
asgiref==3.8.1
Django==5.2.7
pillow==12.0.0
sqlparse==0.5.3
tzdata==2025.2
```

### 4. Navegar al directorio del proyecto

```bash
cd portafolio_6
```

---

## ⚙️ Configuración

### 1. Crear carpetas necesarias

```bash
mkdir media
mkdir static
```

### 2. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Crear superusuario

```bash
python manage.py createsuperuser
```

Ingresa los datos solicitados:
- Username
- Email
- Password

### 4. Cargar datos de prueba (Opcional)

```bash
python manage.py shell
```

```python
from apps.products.models import Category, Product
from django.contrib.auth.models import User

# Crear categorías
cat1 = Category.objects.create(name="Electrónica", description="Productos electrónicos")
cat2 = Category.objects.create(name="Ropa", description="Vestimenta y accesorios")
cat3 = Category.objects.create(name="Hogar", description="Artículos para el hogar")

# Crear productos de ejemplo
user = User.objects.first()
Product.objects.create(
    name="Laptop HP",
    description="Laptop HP 15 pulgadas, 8GB RAM, 256GB SSD",
    category=cat1,
    price=599.99,
    stock=10,
    created_by=user
)
Product.objects.create(
    name="Camiseta Nike",
    description="Camiseta deportiva Nike talla M",
    category=cat2,
    price=29.99,
    stock=50,
    created_by=user
)

exit()
```

### 5. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

Accede a: **http://127.0.0.1:8000/**

---

## 🎮 Uso

### Navegación Principal

- **Inicio:** `/` - Página principal con presentación del proyecto
- **Productos:** `/products/` - Listado de productos con búsqueda y filtros
- **Categorías:** `/products/categories/` - Gestión de categorías (requiere login)
- **Login:** `/auth/login/` - Inicio de sesión
- **Registro:** `/auth/register/` - Registro de nuevos usuarios
- **Perfil:** `/auth/profile/` - Ver y editar perfil de usuario
- **Admin:** `/admin/` - Panel de administración Django

### Funcionalidades por Rol

#### 👤 Usuario Anónimo
- ✅ Ver listado de productos
- ✅ Ver detalles de productos
- ✅ Buscar y filtrar productos
- ✅ Registrarse
- ✅ Iniciar sesión

#### 🔐 Usuario Autenticado
- ✅ Todo lo anterior, más:
- ✅ Crear productos
- ✅ Editar productos
- ✅ Eliminar productos
- ✅ Gestionar categorías
- ✅ Ver y editar perfil
- ✅ Cerrar sesión

#### 👨‍💼 Administrador (Staff)
- ✅ Todo lo anterior, más:
- ✅ Acceso al panel de administración
- ✅ Gestión completa de usuarios
- ✅ Gestión de permisos
- ✅ Estadísticas y reportes

---

## 📁 Estructura del Proyecto

```
Evaluacion_portafolio_6/
│
├── portafolio_6/                  # Proyecto principal Django
│   ├── portafolio_6/             # Configuración del proyecto
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py           # Configuración principal
│   │   ├── urls.py               # URLs principales
│   │   └── wsgi.py
│   │
│   ├── apps/                     # Aplicaciones del proyecto
│   │   ├── auth_p6/             # App de autenticación
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   │   └── auth_p6/
│   │   │   │       ├── login.html
│   │   │   │       ├── register.html
│   │   │   │       ├── profile.html
│   │   │   │       └── profile_edit.html
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── forms.py          # Formularios de autenticación
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   └── views.py          # Vistas de autenticación
│   │   │
│   │   ├── core_p6/             # App núcleo
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   │   └── core_p6/
│   │   │   │       ├── home.html
│   │   │   │       └── about.html
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   └── views.py          # Vistas principales
│   │   │
│   │   └── products/            # App de productos
│   │       ├── migrations/
│   │       ├── templates/
│   │       │   └── products/
│   │       │       ├── product_list.html
│   │       │       ├── product_detail.html
│   │       │       ├── product_form.html
│   │       │       ├── product_confirm_delete.html
│   │       │       ├── category_list.html
│   │       │       ├── category_form.html
│   │       │       └── category_confirm_delete.html
│   │       ├── __init__.py
│   │       ├── admin.py          # Configuración admin personalizado
│   │       ├── apps.py
│   │       ├── forms.py          # Formularios de productos
│   │       ├── models.py         # Modelos Product y Category
│   │       ├── urls.py
│   │       └── views.py          # Vistas CRUD
│   │
│   ├── templates/               # Templates globales
│   │   └── base.html            # Template base con Bootstrap
│   │
│   ├── static/                  # Archivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── media/                   # Archivos subidos por usuarios
│   │   └── products/            # Imágenes de productos
│   │
│   ├── manage.py                # Utilidad de línea de comandos
│   └── db.sqlite3              # Base de datos SQLite
│
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                  # Archivos ignorados por Git
├── README.md                   # Este archivo
└── FRAMEWORKS_COMPARISON.md    # Comparativa detallada de frameworks
```

---

## ✨ Funcionalidades Implementadas

### 🔐 Sistema de Autenticación

#### Registro de Usuarios
- Formulario personalizado con Bootstrap
- Validación de campos (username, email, password)
- Confirmación de contraseña
- Hasheo seguro de contraseñas
- Redirección automática después del registro

#### Inicio de Sesión
- Formulario de login personalizado
- Validación de credenciales
- Mensajes de error informativos
- Recordar sesión
- Redirección a página anterior

#### Gestión de Perfil
- Visualización de información del usuario
- Edición de datos personales
- Cambio de contraseña
- Historial de actividad

### 📦 Gestión de Productos

#### CRUD Completo
- **Crear:** Formulario con validación, subida de imágenes
- **Leer:** Listado paginado, detalle de producto
- **Actualizar:** Edición de datos existentes
- **Eliminar:** Confirmación antes de borrar

#### Características Avanzadas
- 🔍 Búsqueda por nombre y descripción
- 🏷️ Filtrado por categoría
- 📄 Paginación (9 productos por página)
- 🖼️ Gestión de imágenes con Pillow
- 📊 Indicador de estado de stock
- 💰 Formato de precios
- 🏷️ Sistema de categorías

### 🗂️ Gestión de Categorías

- CRUD completo de categorías
- Relación con productos
- Contador de productos por categoría
- Validación de eliminación

### 🎨 Interfaz de Usuario

- ✅ Diseño responsivo con Bootstrap 5
- ✅ Iconos de Bootstrap Icons
- ✅ Navegación intuitiva
- ✅ Mensajes de feedback
- ✅ Breadcrumbs de navegación
- ✅ Cards modernas
- ✅ Modales de confirmación
- ✅ Alerts informativos

---

## 👨‍💼 Panel de Administración

### Acceso

URL: `http://127.0.0.1:8000/admin/`

Requiere: Usuario con permisos de staff/superusuario

### Funcionalidades

#### Gestión de Productos
- Vista de lista personalizada
- Filtros por categoría, estado y fecha
- Búsqueda por nombre y descripción
- Edición inline del estado (activo/inactivo)
- Campos organizados en secciones
- Asignación automática de usuario creador
- Paginación de 20 elementos

#### Gestión de Categorías
- Lista ordenada alfabéticamente
- Búsqueda por nombre
- Contador de productos asociados
- Historial de cambios

#### Gestión de Usuarios
- CRUD completo de usuarios
- Asignación de permisos
- Grupos de usuarios
- Gestión de staff
- Historial de acciones

---

## ✅ Requerimientos Cumplidos

### 1. ✅ Descripción de características de Django
- [x] Investigación sobre Django
- [x] Ventajas para desarrollo empresarial
- [x] Comparación con Flask y FastAPI
- [x] Documentación en README.md

### 2. ✅ Configuración de proyecto Django
- [x] Uso de `django-admin startproject`
- [x] Uso de `django-admin startapp`
- [x] Estructura modular con 3 aplicaciones
- [x] Configuración en `settings.py`

### 3. ✅ Templates dinámicos
- [x] Sistema de plantillas Django
- [x] Template base con herencia
- [x] Bootstrap 5 integrado
- [x] Contenido dinámico desde base de datos
- [x] Variables de contexto
- [x] Bucles y condicionales

### 4. ✅ Formularios web
- [x] Django Forms personalizados
- [x] Validación de datos
- [x] Estilos Bootstrap
- [x] Mensajes de error
- [x] Almacenamiento en base de datos

### 5. ✅ Autenticación y Autorización
- [x] Sistema de login/logout
- [x] Registro de usuarios
- [x] Decorador `@login_required`
- [x] Control de acceso en templates
- [x] Redirecciones configuradas

### 6. ✅ Admin de usuarios y permisos
- [x] Django Admin habilitado
- [x] Personalización de admin
- [x] Gestión de usuarios
- [x] Sistema de permisos
- [x] Filtros y búsqueda

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 👤 Autor

**Hans Schiess**

- GitHub: [@schiesscl](https://github.com/schiesscl)
- Proyecto: [Evaluacion_portafolio_6](https://github.com/HansSchiess/Evaluacion_portafolio_6)
- LinkedIn: [Hans Schiess](https://www.linkedin.com/in/hans-schiess/)

---

## 🙏 Agradecimientos

- **Talento Digital** - Por la formación en desarrollo web
- **Django Software Foundation** - Por el excelente framework
- **Bootstrap Team** - Por el framework CSS
- Comunidad de Python y Django

---

## 📚 Recursos Adicionales

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Django Tutorial](https://www.djangoproject.com/start/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Comparativa Detallada de Frameworks](FRAMEWORKS_COMPARISON.md)

---

## 🐛 Reporte de Bugs

Si encuentras algún bug, por favor abre un issue en:
https://github.com/HansSchiess/Evaluacion_portafolio_6/issues

---

## 📝 Notas de Versión

### v1.0.0 (2025-10-26)
- ✅ Lanzamiento inicial
- ✅ Sistema completo de autenticación
- ✅ CRUD de productos y categorías
- ✅ Panel de administración personalizado
- ✅ Interfaz responsiva con Bootstrap 5
- ✅ Sistema de búsqueda y filtrado
- ✅ Gestión de imágenes

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**

---

*Desarrollado con ❤️ usando Django y Python por [Hans Schiess](https://github.com/HansSchiess)*
