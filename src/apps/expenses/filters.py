import datetime

import django_filters
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from apps.expenses.models import Expense


class ExpenseDateRangeFilter(django_filters.FilterSet):
    date_range = django_filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = Expense
        fields = ["date_range"]


class ExpenseMonthFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(method="filter_by_month", required=True)
    year = django_filters.NumberFilter(method="filter_by_year")

    class Meta:
        model = Expense
        fields = ["month", "year"]

    def filter_by_month(self, queryset: QuerySet, name: str, value: int) -> QuerySet:
        if not 1 <= value <= 12:
            raise ValidationError("Month must be between 1 and 12.")
        return queryset.filter(date__month=value)

    def filter_by_year(self, queryset: QuerySet, name: str, value: int) -> QuerySet:
        if not value:
            value = datetime.date.today().year
        if value < 1990 or value > 2100:
            raise ValidationError("Year must be between 1990 and 2100.")
        return queryset.filter(date__year=value)
