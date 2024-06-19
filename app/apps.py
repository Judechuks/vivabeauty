from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    # context_processors to pass universal context to all template
    def ready(self):
        from . import context_processors  # Import your context_processors module