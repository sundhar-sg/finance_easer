# Generated by Django 3.2.4 on 2021-07-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedCarpetUp_LMS', '0005_auto_20210707_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdb',
            name='id',
        ),
        migrations.AlterField(
            model_name='usersdb',
            name='firstname',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]