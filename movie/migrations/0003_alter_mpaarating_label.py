# Generated by Django 4.2.9 on 2024-02-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movies_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpaarating',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
