from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .form import IncomeForm
from .models import Income


class IncomeList(LoginRequiredMixin, ListView):
    model = Income
    context_object_name = 'incomes'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        queryset = super(IncomeList, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class IncomeDetail(LoginRequiredMixin, DetailView):
    model = Income
    context_object_name = 'income'


class IncomeCreate(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['amount', 'title', 'date']
    success_url = reverse_lazy('incomes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncomeCreate, self).form_valid(form)


class IncomeUpdate(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ['amount', 'title', 'date']
    success_url = reverse_lazy('incomes')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    context_object_name = 'income'
    success_url = reverse_lazy('incomes')
