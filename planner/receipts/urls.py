from django.urls import path
from .views import ReceiptsList, ReceiptDetail, ReceiptCreate, ReceiptUpdate,DeleteView

urlpatterns = [
    path('', ReceiptsList.as_view(), name='receipts'),
    path('receipt/<int:pk>', ReceiptDetail.as_view(), name='receipt'),
    path('receipt-create/', ReceiptCreate.as_view(), name='receipt-create'),
    path('receipt-update/<int:pk>', ReceiptUpdate.as_view(), name='receipt-update'),
    path('receipt-delete/<int:pk>', DeleteView.as_view(), name='receipt-delete'),

]