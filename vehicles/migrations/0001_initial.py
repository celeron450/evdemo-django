# Generated by Django 3.0.4 on 2020-03-09 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='vehicles.Make')),
            ],
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trims', to='vehicles.Model')),
            ],
        ),
    ]