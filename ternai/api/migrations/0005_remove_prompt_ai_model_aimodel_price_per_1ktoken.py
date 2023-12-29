# Generated by Django 4.2.8 on 2023-12-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_externalcall_json_payload_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompt',
            name='ai_model',
        ),
        migrations.AddField(
            model_name='aimodel',
            name='price_per_1ktoken',
            field=models.DecimalField(decimal_places=6, default=0.002, max_digits=7),
            preserve_default=False,
        ),
    ]
