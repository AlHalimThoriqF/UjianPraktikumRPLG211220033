# Generated by Django 5.0.2 on 2024-11-19 10:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peripheral', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headset',
            old_name='nirkabel',
            new_name='mikrofon',
        ),
        migrations.RemoveField(
            model_name='headset',
            name='surround_sound',
        ),
        migrations.AddField(
            model_name='headset',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='headset',
            name='koneksi',
            field=models.CharField(choices=[('jack', '3.5mm Jack'), ('usb', 'USB'), ('bluetooth', 'Bluetooth')], default='jack', max_length=50),
        ),
        migrations.AddField(
            model_name='headset',
            name='kualitas_suara',
            field=models.CharField(choices=[('stereo', 'Stereo'), ('surround', 'Surround'), ('mono', 'Mono')], default='stereo', max_length=50),
        ),
        migrations.AddField(
            model_name='headset',
            name='tipe',
            field=models.CharField(choices=[('wired', 'Wired'), ('wireless', 'Wireless')], default='wired', max_length=10),
        ),
        migrations.AddField(
            model_name='headset',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='headset',
            name='harga',
            field=models.IntegerField(),
        ),
    ]
