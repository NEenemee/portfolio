# Generated by Django 5.1.2 on 2024-11-05 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_job_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-Relavance', '-StartDate']},
        ),
    ]