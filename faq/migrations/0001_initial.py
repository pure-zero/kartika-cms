# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_apphooks_config.fields
import app_data.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('question', models.TextField(blank=True, default='')),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='FaqConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type', models.CharField(verbose_name='type', max_length=100)),
                ('namespace', models.CharField(unique=True, verbose_name='instance namespace', max_length=100, default=None)),
                ('app_data', app_data.fields.AppDataField(editable=False, default='{}')),
                ('paginate_by', models.PositiveIntegerField(verbose_name='Paginate size', default=5)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Apphook configs',
                'verbose_name': 'Apphook config',
            },
        ),
        migrations.AlterUniqueTogether(
            name='faqconfig',
            unique_together=set([('type', 'namespace')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', to='faq.FaqConfig'),
        ),
    ]
