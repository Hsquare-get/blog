# Generated by Django 3.1 on 2020-09-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20200829_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='useremail',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='userpassword',
            field=models.CharField(max_length=16),
        ),
    ]
