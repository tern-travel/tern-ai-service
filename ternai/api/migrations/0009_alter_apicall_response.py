# Generated by Django 4.2.8 on 2023-12-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_endpoint_id_externalcall_endpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicall',
            name='response',
            field=models.JSONField(),
        ),
    ]
