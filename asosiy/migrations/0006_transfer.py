# Generated by Django 4.2.6 on 2023-11-05 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_delete_transfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.PositiveIntegerField()),
                ('tah_narx', models.PositiveIntegerField()),
                ('eski', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sotuvlari', to='asosiy.player')),
                ('mavsum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.hmavsum')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.player')),
                ('yangi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olganlari', to='asosiy.player')),
            ],
        ),
    ]
