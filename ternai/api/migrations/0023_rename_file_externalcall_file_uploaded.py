# Generated by Django 4.2.8 on 2024-01-01 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_externalcall_text_payload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalcall',
            old_name='file',
            new_name='file_uploaded',
        ),
    ]
