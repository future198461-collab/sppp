from django.core.exceptions import ValidationError


def validate_file_size(file_obj, max_mb: int = 3) -> None:
    if not file_obj:
        return
    limit = max_mb * 1024 * 1024
    if getattr(file_obj, "size", 0) > limit:
        raise ValidationError(f"File too large. Max size is {max_mb}MB.")


def upload_to_part_attachment(instance, filename: str) -> str:
    return f"parts/{instance.part_id}/{filename}"
