# Generated by Django 4.2.6 on 2023-11-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='realease_date',
            new_name='release_date',
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
