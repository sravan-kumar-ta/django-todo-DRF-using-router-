# Generated by Django 3.2.9 on 2021-12-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_task_name_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
