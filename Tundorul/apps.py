from django.apps import AppConfig


class TundorulConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tundorul'

    def ready(self):
        from jobs import schedule_updater
        schedule_updater.start()