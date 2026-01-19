from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "action",
        "object_type",
        "object_id",
        "user",
    )
    list_filter = ("action", "object_type")
    search_fields = ("object_id", "message")
    ordering = ("-created_at",)
