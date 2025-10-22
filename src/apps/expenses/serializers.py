from rest_framework import serializers
from django.core.validators import MinValueValidator
from apps.expenses.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        model = Expense
        fields = "__all__"
