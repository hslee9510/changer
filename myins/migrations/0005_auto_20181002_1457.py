# Generated by Django 2.1.1 on 2018-10-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myins', '0004_auto_20181002_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspiration',
            name='Product',
        ),
        migrations.AddField(
            model_name='inspiration',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
