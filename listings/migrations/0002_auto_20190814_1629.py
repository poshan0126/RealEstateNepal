# Generated by Django 2.2.4 on 2019-08-14 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_publishde',
            new_name='is_published',
        ),
    ]
