from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'  # ← AGREGAR 'apps.'
    verbose_name = 'Productos'
