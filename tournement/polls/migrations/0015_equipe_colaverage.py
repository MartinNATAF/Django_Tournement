# Generated by Django 4.1.4 on 2022-12-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_equipe_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='colaverage',
            field=models.IntegerField(default=0),
        ),
    ]
