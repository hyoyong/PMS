# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0013_auto_20170410_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
