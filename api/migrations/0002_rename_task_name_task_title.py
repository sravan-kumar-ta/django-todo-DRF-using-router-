# Generated by Django 3.2.9 on 2021-12-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='title',
        ),
    ]
