# Generated by Django 4.1.2 on 2023-07-29 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_remove_conduitrun_conduitrun_conduitrun_conduit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cablerun',
            name='cable',
        ),
        migrations.RemoveField(
            model_name='conduitrun',
            name='cable',
        ),
        migrations.RemoveField(
            model_name='conduitrun',
            name='conduit',
        ),
        migrations.DeleteModel(
            name='Cable',
        ),
        migrations.DeleteModel(
            name='CableRun',
        ),
        migrations.DeleteModel(
            name='Conduit',
        ),
        migrations.DeleteModel(
            name='ConduitRun',
        ),
    ]
