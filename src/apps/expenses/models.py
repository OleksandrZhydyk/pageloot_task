from django.db import models

from apps.accounts.models import User


class ExpenseCategory(models.TextChoices):
    FOOD = "FOOD"
    TRAVEL = "TRAVEL"
    UTILITIES = "UTILITIES"


class Expense(models.Model):
    user = models.ForeignKey(User, related_name="expenses", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=ExpenseCategory.choices)
