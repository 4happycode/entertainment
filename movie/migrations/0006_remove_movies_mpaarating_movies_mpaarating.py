# Generated by Django 4.2.9 on 2024-02-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movies_imgpath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='mpaaRating',
        ),
        migrations.AddField(
            model_name='movies',
            name='mpaaRating',
            field=models.ManyToManyField(to='movie.mpaarating'),
        ),
    ]
