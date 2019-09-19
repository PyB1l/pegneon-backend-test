# -*- coding: utf-8 -*-
"""`core.models.employee` module.

Provides Employee DB model.
"""

from core.models import mixins
from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.utils.text import slugify


class Employee(mixins.ShardEnabledMixin, mixins.OrganizationMixin, mixins.LogEnabledMixin, models.Model):
    """Base Employee model.
    """

    MALE = 'male'
    FEMALE = 'female'
    UNDEFINED = 'undefined'

    GENDER_CHOICES = (
        (MALE, _('male')),
        (FEMALE, _('female')),
        (UNDEFINED, _('undefined')),
    )

    first_name = models.CharField(
        max_length=255,
        help_text=_('First name')
    )

    last_name = models.CharField(
        max_length=255,
        help_text=_('First name')
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default=UNDEFINED
    )

    active = models.BooleanField(
        default=True,
        help_text=_('Active Employee')
    )

    @property
    def serial(self):
        return str(self.id)

    @property
    def full_name(self):
        """Display employee full name.
        """
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name_plural = _('Employees')

    def __str__(self):
        return f'Employee({self.full_name})'

    __repr__ = __str__
