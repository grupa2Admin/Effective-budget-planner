from django.shortcuts import render, redirect
from .form import IncomeForm
from .models import Income
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IncomeList(LoginRequiredMixin, ListView):
    model = Income
    context_object_name = 'incomes'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = context['incomes'].filter(user=self.request.user)
        return context


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
