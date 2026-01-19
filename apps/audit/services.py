from typing import Optional
from django.contrib.auth import get_user_model

from .models import AuditLog

User = get_user_model()


def log_action(
    *,
    action: str,
    object_type: str,
    object_id: Optional[str] = None,
    user: Optional[User] = None,
    message: str = "",
):
    """
    Central audit logging helper.
    Safe to call from anywhere (views, services, signals).
    """

    AuditLog.objects.create(
        action=action,
        object_type=object_type,
        object_id=object_id,
        user=user,
        message=message,
    )
