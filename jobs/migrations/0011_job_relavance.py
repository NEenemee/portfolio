# Generated by Django 5.1.2 on 2024-11-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Relavance',
            field=models.BooleanField(default=True),
        ),
    ]
