# -*- coding: utf-8 -*-
"""`api.v1.filtersets.department`.

Provides FilterSets for Department ViewSets v1 API.
"""

from core.models import Department
from django_filters import rest_framework as filters


class DepartmentFilter(filters.FilterSet):
    """A custom filterSet for Department ViewSet
    implementing Company search
    """
    class Meta:
        model = Department
        fields = {
            'company_id': [
                'in',
                'exact'
            ]
        }
