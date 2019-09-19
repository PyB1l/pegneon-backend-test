"""pegneon_backend URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin Urls
    path('admin/', admin.site.urls),

    # API Urls
    path('api/', include('api.urls')),

    # Dashboard Urls
    path('', include('dashboard.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
