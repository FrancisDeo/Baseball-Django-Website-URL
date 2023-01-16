# Generated by Django 4.1.5 on 2023-01-15 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dorm_latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('dorm_longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('height', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('weight', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_no', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=False, verbose_name='Zoning Fee')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.person')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.club')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.person'),
        ),
    ]
