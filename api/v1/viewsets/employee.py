# -*- coding: utf-8 -*-
"""`api.v1.viewsets.employee` module.

Provides Employee ViewSets for v1 API.
"""

from api.v1.filtersets.employee import EmployeeFilter
from api.v1.serializers import EmployeeSerializer
from core.models import Employee
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters


class EmployeeViewSet(ListCreateAPIView, DestroyAPIView, GenericViewSet):
    """ViewSet for Employee Entity.
    """

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    filter_class = EmployeeFilter

    filter_backends = (SearchFilter, filters.DjangoFilterBackend, OrderingFilter)

    search_fields = ('first_name', 'last_name', 'active')

    ordering_fields = ('first_name', 'last_name', 'active')

    def get_queryset(self):
        """Prefetch related
        """

        queryset = self.queryset.select_related('company', 'department')

        return queryset
