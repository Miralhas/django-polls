# Generated by Django 4.2.6 on 2023-10-30 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_poll_number_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='complete',
        ),
    ]
