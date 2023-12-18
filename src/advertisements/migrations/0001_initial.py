# Generated by Django 3.0.5 on 2022-03-14 00:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('text', models.TextField()),
                ('url', models.URLField(default='')),
                ('num_clicked', models.IntegerField(default=0)),
                ('clicked', models.ManyToManyField(blank=True, related_name='clicked', to='profiles.Profile')),
                ('reported', models.ManyToManyField(blank=True, related_name='reported', to='profiles.Profile')),
            ],
        ),
    ]
