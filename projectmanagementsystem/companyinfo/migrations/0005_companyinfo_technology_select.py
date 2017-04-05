# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0004_auto_20170405_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='technology_select',
            field=models.CharField(default='', max_length=3, choices=[(b'AU', b'AUTOMOTIVE'), (b'CE', b'CONSUMER'), (b'IOT', b'IOT')]),
            preserve_default=False,
        ),
    ]
