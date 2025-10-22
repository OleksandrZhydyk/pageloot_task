from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.password_validation import validate_password


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields) -> "User":
        if not email:
            raise ValueError("The Email must be set")

        validate_password(password)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(_("username"), max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.username} {self.email}"
