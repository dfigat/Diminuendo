# Generated by Django 5.0.5 on 2024-05-10 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatchMe', '0009_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='id_project',
        ),
    ]