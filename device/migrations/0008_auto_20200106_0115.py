# Generated by Django 2.2 on 2020-01-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_auto_20200106_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='conf_file',
            field=models.FileField(blank=True, default='123.jpg', max_length=1024, null=True, upload_to='conf_file/', verbose_name='配置文件'),
        ),
    ]
