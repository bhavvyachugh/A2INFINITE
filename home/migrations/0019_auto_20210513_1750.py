# Generated by Django 3.1.7 on 2021-05-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210513_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdetails',
            name='freeForAll',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='freeForAll',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='freeForAll',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='freeForAll',
            field=models.BooleanField(default=False),
        ),
    ]
