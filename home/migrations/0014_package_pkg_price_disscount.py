# Generated by Django 3.1.7 on 2021-05-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_package_pkg_price_disscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='pkg_price_disscount',
            field=models.IntegerField(null=True),
        ),
    ]
