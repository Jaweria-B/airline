# Generated by Django 4.2.6 on 2023-11-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='l_name',
            new_name='last_name',
        ),
    ]