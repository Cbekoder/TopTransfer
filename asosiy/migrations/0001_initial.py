# Generated by Django 4.2.6 on 2023-11-01 07:00

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
                ('nom', models.CharField(max_length=30)),
                ('logo', models.FileField(upload_to='')),
                ('davlat', models.CharField(max_length=30)),
                ('presidend', models.CharField(blank=True, max_length=30)),
                ('coach', models.CharField(blank=True, max_length=30)),
                ('yili', models.DateField(blank=True)),
                ('record_transfer', models.CharField(blank=True, max_length=30)),
                ('record_sotuv', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('davlat', models.CharField(max_length=30)),
                ('tugilgan_sana', models.DateField(blank=True)),
                ('narx', models.PositiveIntegerField()),
                ('pozitsiya', models.CharField(max_length=30)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.club')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.PositiveIntegerField()),
                ('tah_narx', models.PositiveIntegerField()),
                ('mavsum', models.CharField(max_length=10)),
                ('eski', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sotuvlari', to='asosiy.player')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.player')),
                ('yangi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olganlari', to='asosiy.player')),
            ],
        ),
    ]
