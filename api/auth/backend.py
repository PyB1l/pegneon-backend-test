# -*- coding: utf-8 -*-
"""`core.auth.backend` module.

Provides APi Authentication / Authorization mechanism for DRF.
"""


from core.models import Employee
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from typing import Union


class DashboardAuthentication(BaseAuthentication):
    """Dashboard Authentication for DRF.
    """

    def authenticate(self, request):
        """
        Returns a `core.Employee` instance if a correct serial is have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        try:
            user = Employee.objects.get(id=request.session['employee'])
        except (Employee.DoesNotExist, KeyError):
            user = None

        return (user, None) if user else None


class IsDashBoardAuthenticated(BasePermission):
    """DRF permission class for Dashboard
    """
    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Employee)


def api_authenticate(request: Request) -> Union[Employee, None]:
    """Authenticate user from request
    using serial code.
    """

    user_pk = request.data.get('serial') or ''

    if not user_pk.isnumeric():
        return None

    try:
        user = Employee.objects.get(id=user_pk)

    except Employee.DoesNotExist:

        return None

    request.session['employee'] = str(user.id)

    return user
