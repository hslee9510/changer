# Generated by Django 2.1.1 on 2018-10-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myins', '0003_auto_20181002_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='Product',
        ),
        migrations.AddField(
            model_name='wish',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
