# Generated by Django 3.2.7 on 2022-05-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movie/images/'),
        ),
    ]
