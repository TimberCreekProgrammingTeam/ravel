# Generated by Django 4.2 on 2023-05-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0009_rename_contest_team_contests'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='output_description',
            field=models.TextField(blank=True),
        ),
    ]
