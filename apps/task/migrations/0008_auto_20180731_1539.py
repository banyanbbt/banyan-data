# Generated by Django 2.0.7 on 2018-07-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_attachment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(blank=True, choices=[('translation', '翻译'), ('data_cleaning', '数据清洗'), ('label_mark', '短信标注')], db_index=True, max_length=255, null=True, verbose_name='类型'),
        ),
    ]
