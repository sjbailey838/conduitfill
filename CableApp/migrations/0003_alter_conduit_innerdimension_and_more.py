# Generated by Django 4.1.2 on 2024-01-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CableApp', '0002_conduit_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conduit',
            name='InnerDimension',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='conduit',
            name='OuterDimension',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
