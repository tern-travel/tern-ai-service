# Generated by Django 4.2.8 on 2023-12-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_apicall_source_call_endpoint_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
