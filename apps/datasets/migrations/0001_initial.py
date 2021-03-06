# Generated by Django 2.0.7 on 2018-09-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datasets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='数据集名称')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='imgs', verbose_name='图片')),
                ('bbn_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='BBN价格')),
                ('description', models.TextField(blank=True, null=True, verbose_name='数据集描述')),
                ('release_at', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('download_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='已下载次数')),
                ('dataset_type', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='数据集类型')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='数据集状态')),
                ('created_by', models.IntegerField(blank=True, default=0, null=True, verbose_name='创建人ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '数据集',
                'verbose_name_plural': '数据集',
                'db_table': 'datasets',
            },
        ),
    ]
