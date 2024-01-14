from django.apps import AppConfig


class LibraryappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libraryapp'
    
    def ready(self):
        '''
        Use ready hook to run code on deploy
        '''
        return
