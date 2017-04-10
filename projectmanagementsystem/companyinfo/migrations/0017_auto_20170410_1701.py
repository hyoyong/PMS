# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0016_companyinfo_technology_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='technology_select',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
