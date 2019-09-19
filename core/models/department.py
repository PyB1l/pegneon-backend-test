# -*- coding: utf-8 -*-
"""`core.models.department` module.

Provides Department DB model.
"""

from core.models import mixins
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Department(mixins.ShardEnabledMixin, mixins.LogEnabledMixin, models.Model):
    """Base Department model.
    """

    name = models.CharField(
        max_length=255,
        help_text=_('Department name')
    )

    slug = models.SlugField(
        blank=True,
        null=False,
        help_text=_('Department slug')
    )

    company = models.ForeignKey(
        'core.Company',
        on_delete=models.CASCADE,
        help_text=_('Department company')
    )

    class Meta:
        verbose_name_plural = _('Departments')
        ordering = ('name',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """Override save method
        """
        if not self.slug:
            self.slug = slugify(f'{self.company.slug}-{self.name}')

        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'Department(name={self.name}, company={self.company.name})'

    __repr__ = __str__
