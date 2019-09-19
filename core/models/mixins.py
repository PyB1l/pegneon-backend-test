# -*- coding: utf-8 -*-
"""`core.models.mixins` module.

Provides core app models re-usable blocks.
"""

from core.db import fields as custom_fields
from django.db import models
from django.utils.translation import gettext_lazy as _


class ShardEnabledMixin(models.Model):
    """Attach Unique Shard ID to model
    """
    id = custom_fields.ShardIDField(
        primary_key=True,
        help_text=_('Unique Shard ID')
    )

    class Meta:
        abstract = True


class LogEnabledMixin(models.Model):
    """Attach created / updated fields to model
    """

    created = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationMixin(models.Model):
    """Attach company / department relations to model
    """

    company = models.ForeignKey(
        'core.Company',
        on_delete=models.CASCADE,
        help_text=_('Company')
    )

    department = models.ForeignKey(
        'core.Department',
        on_delete=models.CASCADE,
        help_text=_('Department')
    )

    class Meta:
        abstract = True
