# -*- coding: utf-8 -*-
"""`api.v1.router`.

Provides router for v1 API.
"""
from api.v1.viewsets.department import DepartmentViewSet
from api.v1.viewsets.employee import EmployeeViewSet
from api.v1.viewsets.challenge import ChallengeViewSet
from rest_framework.routers import SimpleRouter

api_v1 = SimpleRouter()

api_v1.register(r'v1/departments', DepartmentViewSet)
api_v1.register(r'v1/employees', EmployeeViewSet)
api_v1.register(r'v1/challenge', ChallengeViewSet,  basename='challenge')
