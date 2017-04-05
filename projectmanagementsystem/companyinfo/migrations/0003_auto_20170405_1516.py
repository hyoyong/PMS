# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0002_auto_20170405_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='aaaa',
            new_name='name',
        ),
    ]
