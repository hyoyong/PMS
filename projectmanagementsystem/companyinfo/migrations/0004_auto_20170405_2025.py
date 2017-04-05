# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0003_auto_20170405_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='companyinfo',
            name='title',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='business',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='contact',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='position',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='reference',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='url',
            field=models.URLField(),
        ),
    ]
