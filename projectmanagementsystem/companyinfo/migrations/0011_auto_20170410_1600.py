# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0010_auto_20170410_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='business',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='contact',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='hits',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='position',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='reference',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
