# -*- coding: utf-8 -*-
"""`core.db.fields` module.

Provides core app DB field validators.
"""

from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def year_validator(value: str):
    """Validate string for valid year format
    """
    try:
        datetime.strptime(value, '%Y')
    except ValueError:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        ) from None
