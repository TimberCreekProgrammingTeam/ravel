# Generated by Django 4.2 on 2023-10-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0042_contest_show_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input_sum',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output_sum',
            field=models.TextField(default=''),
        ),
    ]