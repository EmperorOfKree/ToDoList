# Generated by Django 2.1.7 on 2019-03-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190317_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='conclusion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='delete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
