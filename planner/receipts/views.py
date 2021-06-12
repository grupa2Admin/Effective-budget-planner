from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .form import ReceiptForm
from .models import Receipt


class ReceiptsList(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = 'receipts'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ReceiptsList, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class ReceiptDetail(LoginRequiredMixin, DetailView):
    model = Receipt
    context_object_name = 'receipt'


class ReceiptCreate(LoginRequiredMixin, CreateView):
    model = Receipt
    fields = ['title', 'description', 'date', 'image']
    success_url = reverse_lazy('receipts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReceiptCreate, self).form_valid(form)


class ReceiptUpdate(LoginRequiredMixin, UpdateView):
    model = Receipt
    fields = ['title', 'description', 'date', 'image']
    success_url = reverse_lazy('receipts')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt
    context_object_name = 'receipt'
    success_url = reverse_lazy('receipts')
