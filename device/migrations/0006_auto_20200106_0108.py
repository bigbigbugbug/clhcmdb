# Generated by Django 2.2 on 2020-01-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0005_auto_20200106_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='conf_file',
            field=models.FileField(default='123.jpg', null=True, upload_to='conf_file/', verbose_name='配置文件'),
        ),
    ]