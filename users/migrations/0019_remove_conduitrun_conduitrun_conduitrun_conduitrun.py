# Generated by Django 4.1.2 on 2023-07-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_cablerun_cablerun_cablerun_cablerun'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conduitrun',
            name='conduitrun',
        ),
        migrations.AddField(
            model_name='conduitrun',
            name='conduitrun',
            field=models.ManyToManyField(to='users.conduit'),
        ),
    ]
