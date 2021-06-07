from .models import Expense
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ExpensesList(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = 'expenses'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = context['expenses'].filter(user=self.request.user)
        return context


class ExpenseDetail(LoginRequiredMixin, DetailView):
    model = Expense
    context_object_name = 'expense'


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'date', 'category']
    success_url = reverse_lazy('expenses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExpenseCreate, self).form_valid(form)


class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['title', 'amount', 'description', 'date', 'category']
    success_url = reverse_lazy('expenses')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = 'expense'
    success_url = reverse_lazy('expenses')
