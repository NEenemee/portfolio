# Generated by Django 5.1.2 on 2024-10-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=' ', max_length=2000),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]