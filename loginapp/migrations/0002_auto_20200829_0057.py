# Generated by Django 3.1 on 2020-08-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='userpassword',
        ),
    ]