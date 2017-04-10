# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0008_companyinfo_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='created_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
