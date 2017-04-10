# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0007_remove_companyinfo_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='hits',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
