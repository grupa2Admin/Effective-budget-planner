from django.shortcuts import render, redirect
from .form import ReceiptForm
from .models import Receipt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ReceiptsList(ListView):
    model = Receipt
    context_object_name = 'receipts'


class ReceiptDetail(DetailView):
    model = Receipt
    context_object_name = 'receipt'


class ReceiptCreate(CreateView):
    model = Receipt
    fields = '__all__'
    success_url = reverse_lazy('receipts')


class ReceiptUpdate(UpdateView):
    model = Receipt
    fields = '__all__'
    success_url = reverse_lazy('receipts')


class DeleteView(DeleteView):
    model = Receipt
    context_object_name = 'receipt'
    success_url = reverse_lazy('receipts')



