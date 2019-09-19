# -*- coding: utf-8 -*-
"""`api.v1.filtersets.employee`.

Provides FilterSets for Employ ViewSets v1 API.
"""

from core.models import Employee
from django_filters import rest_framework as filters


class EmployeeFilter(filters.FilterSet):
    """A custom filterSet for Department ViewSet
    implementing Company search
    """
    class Meta:
        model = Employee
        fields = {
            'company_id': [
                'in',
                'exact'
            ],
            'active': ['exact']
        }
