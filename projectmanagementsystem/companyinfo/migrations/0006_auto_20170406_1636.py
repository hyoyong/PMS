# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0005_companyinfo_technology_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='created_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='business',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='technology_select',
            field=models.CharField(default=b'ALL', max_length=3, choices=[(b'AU', b'AUTOMOTIVE'), (b'CE', b'CONSUMER'), (b'IOT', b'IOT'), (b'ALL', b'ALL')]),
        ),
    ]
