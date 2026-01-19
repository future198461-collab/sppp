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

    list_filter = ("action", "object_type", "created_at")
    search_fields = ("action", "object_type", "object_id", "message")

    ordering = ("-created_at",)

    readonly_fields = (
        "id",
        "user",
        "action",
        "object_type",
        "object_id",
        "message",
        "created_at",
    )
