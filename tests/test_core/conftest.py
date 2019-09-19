# -*- coding: utf-8 -*-
"""core App test suit
"""

from core import factories
from pytest_factoryboy import register

register(factories.CompanyFactory)
register(factories.DepartmentFactory)
register(factories.EmployeeFactory)
