# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0006_auto_20170406_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='cdate',
        ),
    ]
