# Generated by Django 4.1.2 on 2023-07-12 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_cable_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnerDimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InnerDimension', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OuterDimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OuterDimension', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Conduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('InnerDimension', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.innerdimension')),
                ('OuterDimension', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.outerdimension')),
            ],
        ),
    ]