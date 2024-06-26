# Generated by Django 5.0.4 on 2024-04-19 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='episodios',
        ),
        migrations.AddField(
            model_name='episodios',
            name='filme',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='epsodios', to='filme_app.filme'),
        ),
        migrations.AddField(
            model_name='episodios',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episodios',
            name='nome',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
