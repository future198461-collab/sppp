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

    list_filter = (
        "action",
        "object_type",
    )

    search_fields = (
        "object_id",
        "message",
    )

    ordering = ("-created_at",)

    # 🔒 полностью read-only
    readonly_fields = (
        "id",
        "created_at",
        "action",
        "object_type",
        "object_id",
        "user",
        "message",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
