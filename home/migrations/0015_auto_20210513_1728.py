# Generated by Django 3.1.7 on 2021-05-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_package_pkg_price_disscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdetails',
            name='freeForAll',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='freeForAll',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='freeForAll',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='freeForAll',
            field=models.BooleanField(default=True),
        ),
    ]
