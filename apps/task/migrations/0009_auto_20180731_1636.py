# Generated by Django 2.0.7 on 2018-07-31 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20180731_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(blank=True, choices=[('文本', '文本'), ('图片', '图片'), ('音频', '音频'), ('视频', '视频')], db_index=True, max_length=255, null=True, verbose_name='类型'),
        ),
    ]
