# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0014_auto_20170410_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='technology_select',
        ),
    ]
