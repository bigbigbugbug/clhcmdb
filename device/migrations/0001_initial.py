# Generated by Django 2.2 on 2020-01-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='交换机名称')),
                ('ip', models.TextField(max_length=32, verbose_name='IP地址')),
                ('position', models.TextField(max_length=256, verbose_name='交换机位置')),
                ('description', models.TextField(max_length=1024, verbose_name='描述')),
            ],
            options={
                'verbose_name': '交换机',
                'verbose_name_plural': '交换机信息',
            },
        ),
    ]