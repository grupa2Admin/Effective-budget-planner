from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Expense


class ExpensesList(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = 'expenses'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ExpensesList, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


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
