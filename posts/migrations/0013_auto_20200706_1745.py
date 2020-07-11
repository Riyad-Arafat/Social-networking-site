# Generated by Django 3.0.6 on 2020-07-06 15:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_auto_20200702_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]