# Generated by Django 4.2.8 on 2023-12-29 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_response_apicall_response_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apicall',
            old_name='response_JSON',
            new_name='response',
        ),
    ]
