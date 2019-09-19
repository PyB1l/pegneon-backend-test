# -*- coding: utf-8 -*-
"""`core.db.fields` module.

Provides core app DB field custom implementations.
"""

from django.db.models import BigAutoField


class ShardIDField(BigAutoField):
    """Custom unique id across all tables.
    """

    def db_type(self, connection):
        """ Use the sequence to get next value """
        return "bigint NOT NULL DEFAULT public.id_generator()"
