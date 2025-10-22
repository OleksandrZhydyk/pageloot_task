from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.expenses.views import ExpensesByCategoryApiView, ExpensesDateRangeApiView, ExpensesViewSet

router = DefaultRouter()

router.register("expenses", ExpensesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("expenses/by-range/<int:user_id>", ExpensesDateRangeApiView.as_view()),
    path("expenses/by-category/<int:user_id>", ExpensesByCategoryApiView.as_view()),
]
