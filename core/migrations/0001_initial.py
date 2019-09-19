# -*- coding: utf-8 -*-
"""`core.models.company` module.

Provides Company DB model.
"""

import core.db.operations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        core.db.operations.CreateShardID(),
    ]
