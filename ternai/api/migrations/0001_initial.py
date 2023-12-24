# Generated by Django 5.0 on 2023-12-24 17:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AIModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('context_window', models.IntegerField()),
                ('api_value', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='APICall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prompt_text', models.TextField()),
                ('in_progress', models.BooleanField()),
                ('complete', models.BooleanField()),
                ('response', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Endpoints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalCall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('webhook_url', models.URLField()),
                ('json_payload', models.JSONField()),
                ('endpoint_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.endpoints')),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('instructions', models.TextField()),
                ('ai_model', models.CharField(help_text='The OpenAI Model to Use (e.g.gpt-3.5-turbo-0613)', max_length=256)),
                ('example_response', models.TextField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.RestrictedError, to='api.aimodel')),
            ],
        ),
        migrations.AddField(
            model_name='endpoints',
            name='prompt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RestrictedError, to='api.prompt'),
        ),
    ]