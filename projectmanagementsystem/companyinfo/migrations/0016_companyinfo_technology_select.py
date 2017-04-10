# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0015_remove_companyinfo_technology_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='technology_select',
            field=models.CharField(default=b'ALL', max_length=3, choices=[(b'AU', b'AUTOMOTIVE'), (b'CE', b'CONSUMER'), (b'IOT', b'IOT'), (b'ALL', b'ALL')]),
        ),
    ]
