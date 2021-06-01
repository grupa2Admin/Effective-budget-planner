"""HomeBudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from dashboard import views

from dashboard.views import PasswordsChangeView, UserEditView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
logo_view = RedirectView.as_view(url='/static/logo.png', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    re_path(r'^logo\.png$', logo_view),
    path('', views.main, name="main"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registerPage, name='register'),
    path('password-reset/', views.forgotPasswordPage, name='forgot_password'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile')
]

# To be done later #
# path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
#      name='password_reset'),
# path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
#     template_name='registration/password_reset_done.html'), name='password_reset_done'),
#     path('password-reset/', auth_views.PasswordResetView, name='forgot_password'),
