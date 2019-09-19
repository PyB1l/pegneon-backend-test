# -*- coding: utf-8 -*-
"""`api.v1.serializers`.

Provides Model Serializers for v1 API.
"""


from core.models import Company, Department, Employee
from rest_framework.serializers import ModelSerializer, IntegerField


class CompanyBaseSerializer(ModelSerializer):
    """`core.Company` Serializer for v1 API.
    """

    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'founded_at')


class DepartmentSerializer(ModelSerializer):
    """`core.Department` Serializer for v1 API.
    """

    company = CompanyBaseSerializer(read_only=True)
    company_id = IntegerField(write_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'slug', 'company', 'company_id', 'created', 'modified')
        extra_kwargs = {
            'created': {'read_only': True},
            'modified': {'read_only': True},
        }


class EmployeeSerializer(ModelSerializer):
    """`core.Employee` Serializer for v1 API.
    """

    company = CompanyBaseSerializer(read_only=True)
    company_id = IntegerField(write_only=True)

    department = DepartmentSerializer(read_only=True)
    department_id = IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'gender', 'company', 'department', 'company_id', 'department_id',
                  'created', 'modified', 'active')
        extra_kwargs = {
            'created': {'read_only': True},
            'modified': {'read_only': True},
        }