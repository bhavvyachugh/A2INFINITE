# Generated by Django 3.1.7 on 2021-05-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdetails',
            name='freeForAll',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='explain',
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