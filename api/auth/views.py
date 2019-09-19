# -*- coding: utf-8 -*-
"""`core.auth.views` module.

Provides API Authentication / Authorization views.
"""

from core.models import Employee
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class LoginView(APIView):
    """API login View
    """

    def post(self, request: Request) -> Response:
        """Authenticate user
        """
        try:
            user = Employee.objects.get(id=request.data.get('serial'))

        except Employee.DoesNotExist:
            return Response(
                data={'Error': 'Unable to authenticate provided credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.session['employee'] = str(user.id)

        return Response(data={
            'success': request.session['employee']
        })


class LogoutView(APIView):
    """API login View
    """

    def get(self, request: Request) -> Response:
        """Authenticate user
        """
        try:
            del request.session['employee']
        except KeyError:
            pass

        return Response(data={
            'success': '/api/login'
        })
