# Generated by Django 4.1.2 on 2023-07-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_conduitrun'),
    ]

    operations = [
        migrations.AddField(
            model_name='conduitrun',
            name='cablerun',
            field=models.ManyToManyField(to='users.cablerun'),
        ),
    ]