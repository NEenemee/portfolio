# Generated by Django 5.1.2 on 2024-11-05 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_education_job_current'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-EndDate']},
        ),
    ]
