# -*- coding: utf-8 -*-
"""`dashboard.views` module.

Provides dashboard App views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index_view(request: HttpRequest) -> HttpResponse:
    """Redirect to game page
    """

    return redirect('game-view')


def game_view(request: HttpRequest) -> HttpResponse:
    """Game View
    """

    return render(request, context={}, template_name='dashboard/login.html')
