# -*- coding: utf-8 -*-
"""`core.factories` module.

Provides core.models factories for Unit testing.
"""


import factory
from core.models import Company, Department, Employee


class CompanyFactory(factory.DjangoModelFactory):
    """Fixture for Company model
    """
    name = factory.Sequence(lambda n: f'Test Company {n}')
    slug = factory.Sequence(lambda n: f'test-company-{n}')

    class Meta:
        model = Company


class DepartmentFactory(factory.DjangoModelFactory):
    """Fixture for Department model.
    """

    name = factory.Sequence(lambda n: f'Test department {n}')
    slug = factory.Sequence(lambda n: f'test-department-{n}')

    company = factory.RelatedFactory(CompanyFactory)

    class Meta:
        model = Department


class EmployeeFactory(factory.DjangoModelFactory):
    """Fixture for Employee model.
    """
    fist_name = factory.Sequence(lambda n: f'Employee {n} name')
    last_name = factory.Sequence(lambda n: f'Employee {n} last name')
    gender = 'undefined'
    company = factory.RelatedFactory(CompanyFactory)
    department = factory.RelatedFactory(DepartmentFactory)

    class Meta:
        model = Employee
