# Generated by Django 4.2.8 on 2024-01-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_file_externalcall_file_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='largest_token_model',
            field=models.BooleanField(default=False),
        ),
    ]
