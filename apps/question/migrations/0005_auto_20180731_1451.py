# Generated by Django 2.0.7 on 2018-07-31 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(blank=True, choices=[('unresolved', '未解决'), ('resolved', '已解决')], max_length=255, null=True, verbose_name='状态'),
        ),
    ]
