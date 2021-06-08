from django.shortcuts import render, redirect
from .form import ReceiptForm
from .models import Receipt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ReceiptsList(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = 'receipts'
    ordering = ['-date']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receipts'] = context['receipts'].filter(user=self.request.user)

        return context


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
