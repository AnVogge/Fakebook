# Generated by Django 3.0.5 on 2022-09-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0004_configuration_profiles_friends_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='relationship_management_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
