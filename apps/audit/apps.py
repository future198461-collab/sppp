from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in, user_logged_out


class AuditConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.audit"

    def ready(self):
        from .services import log_action

        user_logged_in.connect(
            lambda sender, request, user, **kwargs: log_action(
                action="login",
                object_type="user",
                object_id=str(user.id),
                user=user,
                message="User logged in",
            )
        )

        user_logged_out.connect(
            lambda sender, request, user, **kwargs: log_action(
                action="logout",
                object_type="user",
                object_id=str(user.id),
                user=user,
                message="User logged out",
            )
        )
