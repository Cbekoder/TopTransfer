# Generated by Django 4.2.6 on 2023-11-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_alter_club_presidend'),
    ]

    operations = [
        migrations.CreateModel(
            name='HMavsum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hozirgi_mavsum', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Hozirgi Mavsum',
                'verbose_name_plural': 'Hozirgi Mavsum',
            },
        ),
    ]
