from django.core.cache import cache
from django.db import models
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.expenses.filters import ExpenseDateRangeFilter, ExpenseMonthFilter
from apps.expenses.serializers import ExpenseSerializer
from apps.expenses.models import Expense
from rest_framework.viewsets import ModelViewSet


class ExpensesViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpensesDateRangeApiView(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseDateRangeFilter

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        user_id = self.kwargs.get("user_id")
        queryset = queryset.filter(user_id=user_id)
        return queryset


class ExpensesByCategoryApiView(APIView):
    queryset = Expense.objects.all()

    def get(self, request: Request, user_id: int) -> Response:
        month = request.GET.get("month", "")
        year = request.GET.get("year", "")
        cache_key = f"expenses_user_{user_id}_{month}_{year}"
        data = cache.get(cache_key)
        if not data:
            filtered_qs = ExpenseMonthFilter(request.GET, queryset=self.queryset).qs
            data = filtered_qs.filter(user_id=user_id).values("category").annotate(expenses=models.Sum("amount"))
            cache.set(cache_key, data, timeout=60 * 5)
        return Response(data=data)
