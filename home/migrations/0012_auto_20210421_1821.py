# Generated by Django 3.1.7 on 2021-04-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210421_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='feature_1',
            new_name='pkg_feature_1',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='feature_10',
            new_name='pkg_feature_2',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='feature_11',
            new_name='pkg_feature_3',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='feature_12',
            new_name='pkg_feature_4',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='feature_2',
            new_name='pkg_feature_5',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='feature_3',
            new_name='pkg_feature_6',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_4',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_5',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_6',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_7',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_8',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature_9',
        ),
    ]