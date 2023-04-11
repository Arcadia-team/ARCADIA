from django.apps import AppConfig


class AppIndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_index'


class CreateUserProfile(AppConfig):
    name = 'app_index'
    
    def ready(self):
        # Importa tus señales aquí
        import app_index.post_save 
