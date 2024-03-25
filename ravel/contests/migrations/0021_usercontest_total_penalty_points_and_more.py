# Generated by Django 4.2 on 2023-05-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0020_userproblem_solve_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontest',
            name='total_penalty_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usercontest',
            name='total_solves',
            field=models.IntegerField(default=0),
        ),
    ]