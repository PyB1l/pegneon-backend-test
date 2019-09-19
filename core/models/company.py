# -*- coding: utf-8 -*-
"""`core.models.company` module.

Provides Company DB model.
"""

from core.db.validators import year_validator
from core.models import mixins
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Company(mixins.ShardEnabledMixin, mixins.LogEnabledMixin, models.Model):
    """Base company model.
    """

    name = models.CharField(
        max_length=255,
        help_text=_('Company name')
    )

    slug = models.SlugField(
        blank=True,
        null=False,
        help_text=_('Company slug')
    )

    founded_at = models.CharField(
        blank=True,
        null=True,
        max_length=4,
        help_text=_('Company founded year'),
        validators=[year_validator]
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """Override save method
        """
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name_plural = _('Companies')
        ordering = ('name', )

    def __str__(self):
        return f'Company(name={self.name})'

    __repr__ = __str__
