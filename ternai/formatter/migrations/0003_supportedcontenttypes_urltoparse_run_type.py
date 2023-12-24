# Generated by Django 5.0 on 2023-12-15 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formatter', '0002_urltoparse'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportedContentTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('descriptions', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='urltoparse',
            name='run_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='formatter.supportedcontenttypes'),
            preserve_default=False,
        ),
    ]