from django.apps import AppConfig


class AuthP6Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auth_p6'  # ← AGREGAR 'apps.'
    verbose_name = 'Autenticación'
