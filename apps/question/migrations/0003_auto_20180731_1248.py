# Generated by Django 2.0.7 on 2018-07-31 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20180730_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answeroption',
            options={'verbose_name': '答案选项', 'verbose_name_plural': '答案选项'},
        ),
        migrations.AlterModelTable(
            name='answeroption',
            table='answer_options',
        ),
    ]
