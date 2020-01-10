# Generated by Django 2.2 on 2020-01-07 03:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_auto_20200107_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='conf_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='file/'),
            preserve_default=False,
        ),
    ]