# Generated by Django 2.2.4 on 2019-10-15 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_remove_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]