from django.apps import AppConfig


class CoreP6Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core_p6'  # ← AGREGAR 'apps.'
    verbose_name = 'Núcleo'
