from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from planner import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="administrator"),
    path('', include('dashboard.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
