# Generated by Django 4.2.8 on 2023-12-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_apicall_error_text_apicall_valid_resopnse'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='ai_temperature',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=2),
            preserve_default=False,
        ),
    ]