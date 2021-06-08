from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm, PasswordResetForm
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from receipts.models import Receipt
from expenses.models import Expense
from income.models import Income
from itertools import chain


# Create your views here.

from .forms import RegisterForm, UpdateProfileForm





def main(request):
    return render(request, 'dashboard/background.html')


# Own view for redirecting after changing password

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('main')


class UserEditView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user


class LoginView(auth_views.LoginView):
    form = AuthenticationForm
    template_name = 'registration/login.html'


def registerPage(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('main')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def search_page(request):
    if request.method == "POST":
        searched = request.POST['searched']
        receipt_results = Receipt.objects.filter(title__contains=searched).filter(user=request.user)
        expense_results = Expense.objects.filter(title__contains=searched).filter(user=request.user)
        income_results = Income.objects.filter(title__contains=searched).filter(user=request.user)
        results = chain(receipt_results, expense_results, income_results)
        return render(request, 'dashboard/search_page.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'dashboard/search_page.html', {})