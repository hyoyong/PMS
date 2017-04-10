# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0009_auto_20170410_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='created_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
