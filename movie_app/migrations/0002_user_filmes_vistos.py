# Generated by Django 5.0.4 on 2024-04-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme_app', '0002_remove_filme_episodios_episodios_filme_and_more'),
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='filmes_vistos',
            field=models.ManyToManyField(blank=True, related_name='filmes', to='filme_app.filme'),
        ),
    ]
