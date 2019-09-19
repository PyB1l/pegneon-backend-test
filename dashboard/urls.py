# -*- coding: utf-8 -*-
"""`dashboard.urls` module.

Provides dashboard App urls.
"""

from dashboard import views
from django.urls import path


urlpatterns = [
    # App views
    path('', views.index_view, name='index-view'),
    path('game/', views.game_view, name='game-view'),
]
