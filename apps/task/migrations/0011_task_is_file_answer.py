# Generated by Django 2.0.7 on 2018-08-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_task_max_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_file_answer',
            field=models.BooleanField(default=False, verbose_name='答案是否需要上传文件'),
        ),
    ]
