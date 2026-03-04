"""
URL configuration for voltageauto project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('', include('products.urls_templates')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "VoltageAuto Admin"
admin.site.site_title = "VoltageAuto Admin Portal"
admin.site.index_title = "Welcome to VoltageAuto Administration"
