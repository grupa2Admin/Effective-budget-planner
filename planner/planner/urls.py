from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from planner import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipts/', include('receipts.urls')),
    path('', include('dashboard.urls')),
    path('expenses/', include('expenses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

