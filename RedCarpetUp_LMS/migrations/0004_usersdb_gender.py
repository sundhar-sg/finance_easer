# Generated by Django 3.2.4 on 2021-07-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedCarpetUp_LMS', '0003_auto_20210707_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersdb',
            name='gender',
            field=models.CharField(default='Gender', max_length=10),
        ),
    ]
