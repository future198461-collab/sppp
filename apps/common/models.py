from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = "admin"
    ROLE_BUYER = "buyer"
    ROLE_SUPPLIER = "supplier"

    ROLE_CHOICES = (
        (ROLE_ADMIN, "Admin"),
        (ROLE_BUYER, "Buyer"),
        (ROLE_SUPPLIER, "Supplier"),
    )

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"
