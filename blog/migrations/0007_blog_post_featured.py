# Generated by Django 5.0.6 on 2024-10-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_featuredpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
