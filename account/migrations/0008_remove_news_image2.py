# Generated by Django 3.2.9 on 2021-11-30 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_try_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image2',
        ),
    ]
