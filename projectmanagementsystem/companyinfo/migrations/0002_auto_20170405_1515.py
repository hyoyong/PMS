# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='name',
            new_name='aaaa',
        ),
    ]
