# Generated by Django 4.1.4 on 2022-12-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_equipe_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
