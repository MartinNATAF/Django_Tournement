# Generated by Django 4.1.4 on 2022-12-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_visiteur_equipe_match_score_locaux_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Match',
        ),
    ]
