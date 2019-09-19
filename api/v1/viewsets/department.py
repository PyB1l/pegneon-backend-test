# -*- coding: utf-8 -*-
"""`api.v1.viewsets.department` module.

Provides Department ViewSets for v1 API.
"""

from api.v1.filtersets.department import DepartmentFilter
from api.v1.serializers import DepartmentSerializer
from core.models import Department
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters


class DepartmentViewSet(ListCreateAPIView, GenericViewSet):
    """ViewSet for Department Entity.
    """

    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer

    filter_class = DepartmentFilter

    filter_backends = (SearchFilter, filters.DjangoFilterBackend, OrderingFilter)

    search_fields = ('name', )

    ordering_fields = ('name', )

    def get_queryset(self):
        """Prefetch related
        """

        queryset = self.queryset.prefetch_related('company', 'employee_set')

        return queryset
