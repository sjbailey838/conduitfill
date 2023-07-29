# Generated by Django 4.1.2 on 2023-07-29 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=50, null=True)),
                ('rating', models.CharField(max_length=50, null=True)),
                ('conductors', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CableRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabletag', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('cable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CableApp.cable')),
            ],
        ),
        migrations.CreateModel(
            name='Conduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('InnerDimension', models.CharField(max_length=200, null=True)),
                ('OuterDimension', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConduitRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conduittag', models.CharField(max_length=200)),
                ('cable', models.ManyToManyField(to='CableApp.cablerun')),
                ('conduit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CableApp.conduit')),
            ],
        ),
    ]