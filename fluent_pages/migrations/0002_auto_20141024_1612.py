# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlnode',
            name='key',
            field=models.SlugField(choices=[('concept', 'Le concept'), ('dr-pommereau', 'Dr Xavier Pommereau'), ('formations', 'Nos formations'), ('mentions-legales', 'Mentions l\xe9gales')], blank=True, help_text='A unique identifier that is used for linking to this page.', null=True, verbose_name='page identifier'),
        ),
    ]
