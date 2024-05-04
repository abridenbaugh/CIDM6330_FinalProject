from django.apps import AppConfig


class SuccessionPlansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "succession_plans"

    def ready(self):
        import succession_plans.signals
