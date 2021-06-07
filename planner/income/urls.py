from django.urls import path
from .views import IncomeList, IncomeDetail, IncomeCreate, IncomeUpdate, DeleteView

urlpatterns = [
    path('', IncomeList.as_view(), name='incomes'),
    path('income/<int:pk>', IncomeDetail.as_view(), name='income'),
    path('income-create/', IncomeCreate.as_view(), name='income-create'),
    path('income-update/<int:pk>', IncomeUpdate.as_view(), name='income-update'),
    path('income-delete/<int:pk>', DeleteView.as_view(), name='income-delete'),

]
