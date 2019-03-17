# Generated by Django 2.1.7 on 2019-03-17 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('edit_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField()),
                ('conclusion_date', models.DateTimeField()),
            ],
        ),
    ]