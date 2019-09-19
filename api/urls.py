# -*- coding: utf-8 -*-
"""`api.urls`.

API urls with semantic.
"""

from api.auth import views as auth_views
from api.v1.router import api_v1
from django.urls import path


# Mount Auth

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='api-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='api-logout')
]

# Mount API versions
urlpatterns += api_v1.urls
