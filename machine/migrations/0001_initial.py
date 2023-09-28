# Generated by Django 4.2.5 on 2023-09-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value_x_min', models.FloatField()),
                ('value_x_max', models.FloatField()),
                ('value_y_min', models.FloatField()),
                ('value_y_max', models.FloatField()),
                ('value_z_min', models.FloatField()),
                ('value_z_max', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value_x', models.IntegerField()),
                ('value_y', models.IntegerField()),
                ('value_z', models.IntegerField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.machine')),
                ('measurement_points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.measurementpoint')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.standard')),
            ],
        ),
        migrations.AddField(
            model_name='measurementpoint',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.standard'),
        ),
    ]