# -*- coding: utf-8 -*-
"""`api.v1.viewsets.game` module.

Provides Game ViewSets for v1 API.
"""

from api.auth.backend import DashboardAuthentication, IsDashBoardAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class ChallengeViewSet(GenericViewSet, GenericAPIView):
    """ViewSet for Challenge.
    """

    authentication_classes = [DashboardAuthentication]
    permission_classes = [IsDashBoardAuthenticated]

    def list(self, request):
        """Override List to provide User game response
        """
        return Response(
            data={
                'greetings': f'Hello {request.user.full_name}',
                'company': f'{request.user.company.name}',
                'department': f'{request.user.department.name}',
            },
            status=status.HTTP_200_OK
        )
