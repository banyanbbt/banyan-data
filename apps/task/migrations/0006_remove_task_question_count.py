# Generated by Django 2.0.7 on 2018-07-31 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20180731_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='question_count',
        ),
    ]
