# Generated by Django 2.0.7 on 2018-07-26 11:23

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('task_id', models.IntegerField(verbose_name='任务id')),
                ('question_id', models.IntegerField(verbose_name='题目id')),
                ('content', jsonfield.fields.JSONField(verbose_name='文本结果')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='文件结果')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='状态')),
                ('reviewer_id', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='审核人id')),
            ],
            options={
                'verbose_name_plural': '答案',
                'db_table': 'answers',
                'verbose_name': '答案',
            },
        ),
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('task_id', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='所属任务id')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='输入项名称')),
                ('option_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='输入项类型')),
                ('example', models.CharField(blank=True, max_length=255, null=True, verbose_name='示例内容')),
                ('is_required', models.BooleanField(verbose_name='输入项是否必填')),
                ('position', models.IntegerField(verbose_name='输入项排序')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='状态')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('detail_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='表名称')),
                ('detail_id', models.IntegerField(verbose_name='表ID')),
                ('file_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='附件名称')),
                ('file_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='附件访问地址')),
                ('file_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='附件类型')),
                ('file_size', models.CharField(blank=True, max_length=255, null=True, verbose_name='附件大小')),
            ],
            options={
                'verbose_name_plural': '附件',
                'db_table': 'attachments',
                'verbose_name': '附件',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('task_id', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='所属任务id')),
                ('content', models.TextField(blank=True, null=True, verbose_name='题目内容')),
            ],
            options={
                'verbose_name_plural': '题目',
                'db_table': 'questions',
                'verbose_name': '题目',
            },
        ),
    ]