# Generated by Django 4.2.6 on 2023-11-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='record_sotuv',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='club',
            name='record_transfer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
