# Generated by Django 4.1.2 on 2023-07-19 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_rename_cablerun_cablerun_cable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conduitrun',
            name='conduitrun',
        ),
        migrations.AddField(
            model_name='conduitrun',
            name='conduit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.conduit'),
            preserve_default=False,
        ),
    ]
