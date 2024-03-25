# Generated by Django 4.2 on 2023-05-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0016_remove_userproblem_problem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproblem',
            name='contest_problem',
        ),
        migrations.AddField(
            model_name='userproblem',
            name='problem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contests.problem'),
            preserve_default=False,
        ),
    ]
