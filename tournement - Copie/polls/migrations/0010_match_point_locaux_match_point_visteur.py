# Generated by Django 4.1.4 on 2022-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_match_id_match_match_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='point_locaux',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='point_visteur',
            field=models.IntegerField(default=0),
        ),
    ]