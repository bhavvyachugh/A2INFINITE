# Generated by Django 3.1.7 on 2021-04-05 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210405_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='explain',
            old_name='imgBlackWhite',
            new_name='imgBlack',
        ),
    ]
