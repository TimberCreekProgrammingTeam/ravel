# Generated by Django 4.2 on 2023-06-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contests', '0027_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='contest_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
