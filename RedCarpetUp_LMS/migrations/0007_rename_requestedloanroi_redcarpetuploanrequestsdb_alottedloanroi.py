# Generated by Django 3.2.5 on 2021-07-08 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RedCarpetUp_LMS', '0006_auto_20210707_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redcarpetuploanrequestsdb',
            old_name='requestedloanroi',
            new_name='alottedloanroi',
        ),
    ]
