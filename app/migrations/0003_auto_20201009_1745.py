# Generated by Django 3.0 on 2020-10-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]