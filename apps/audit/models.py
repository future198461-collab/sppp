import uuid

from django.conf import settings
from django.db import models


class AuditLog(models.Model):
    """
    Universal audit log for system actions
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
    )

    action = models.CharField(max_length=100)
    object_type = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, null=True, blank=True)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Audit log"
        verbose_name_plural = "Audit logs"

    def __str__(self):
        return f"{self.action} | {self.object_type} | {self.created_at:%Y-%m-%d %H:%M:%S}"
