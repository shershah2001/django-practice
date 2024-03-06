# Generated by Django 5.0.2 on 2024-03-05 06:19

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50)),
                ('news_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]
