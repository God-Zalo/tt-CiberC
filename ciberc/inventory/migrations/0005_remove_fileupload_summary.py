# Generated by Django 2.2 on 2021-03-12 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210311_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='summary',
        ),
    ]