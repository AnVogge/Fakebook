# Generated by Django 3.0.5 on 2022-02-25 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
    ]
