# Generated by Django 3.0 on 2020-10-09 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201009_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='imagen1',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='imagen2',
            field=models.FileField(upload_to='media/'),
        ),
    ]
