# Generated by Django 4.2.8 on 2024-01-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_delete_apifiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalcall',
            name='text_payload',
            field=models.TextField(blank=True, null=True),
        ),
    ]