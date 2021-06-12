from django.urls import path
from .views import ExpensesList, ExpenseDetail, ExpenseCreate, ExpenseUpdate, DeleteView

urlpatterns = [
    path('', ExpensesList.as_view(), name='expenses'),
    path('expense/<int:pk>', ExpenseDetail.as_view(), name='expense'),
    path('expense-create/', ExpenseCreate.as_view(), name='expense-create'),
    path('expense-update/<int:pk>', ExpenseUpdate.as_view(), name='expense-update'),
    path('expense-delete/<int:pk>', DeleteView.as_view(), name='expense-delete'),
]