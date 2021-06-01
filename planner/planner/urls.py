from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name="administrator"),
    path('', include('dashboard.urls')), ]

# To be completed later #

# path('password-reset/',
#      auth_views.PasswordResetView.as_view(
#          template_name='registration/password_reset.html'
#      ),
#      name='password_reset'),
# path('password-reset/done/',
#      auth_views.PasswordResetDoneView.as_view(
#          template_name='registration/password_reset_done.html'
#      ),
#      name='password_reset_done'),
# path('password-reset-confirm/<uidb64>/<token>/',
#      auth_views.PasswordResetConfirmView.as_view(
#          template_name='registration/password_reset_confirm.html'
#      ),
#      name='password_reset_confirm'),
# path('password-reset-complete/',
#      auth_views.PasswordResetCompleteView.as_view(
#          template_name='registration/password_reset_complete.html'
#      ),
#      name='password_reset_complete'),
