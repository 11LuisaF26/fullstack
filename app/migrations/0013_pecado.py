# Generated by Django 3.0 on 2020-10-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_pelea'),
    ]

    operations = [
        migrations.CreateModel(
            name='pecado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='nombre')),
                ('pecado', models.CharField(blank=True, max_length=100, verbose_name='pecado')),
                ('poder', models.CharField(blank=True, max_length=100, verbose_name='poder')),
                ('imagen', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'pelea',
                'verbose_name_plural': 'peleas',
            },
        ),
    ]
