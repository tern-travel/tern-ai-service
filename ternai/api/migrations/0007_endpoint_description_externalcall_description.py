# Generated by Django 4.2.8 on 2023-12-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_endpoints_endpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='externalcall',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]