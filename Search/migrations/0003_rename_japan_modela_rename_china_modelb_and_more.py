# Generated by Django 4.0.7 on 2023-03-14 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0002_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Japan',
            new_name='ModelA',
        ),
        migrations.RenameModel(
            old_name='China',
            new_name='ModelB',
        ),
        migrations.RenameModel(
            old_name='Nigeria',
            new_name='ModelC',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
