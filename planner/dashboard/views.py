from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
from dashboard.forms import RegisterForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def main(request):
    return render(request, 'dashboard/main.html')


# def LoginPage(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 return redirect('/')
#             else:
#                 messages.info(request, 'Username or password is incorrect')
#
#         context = {}
#         return render(request, 'dashboard/login.html', context)
#
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'dashboard/login.html'


def registerPage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'dashboard/register.html')


def forgotPasswordPage(request):
    return render(request, 'dashboard/password.html')
