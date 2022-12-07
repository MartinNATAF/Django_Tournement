# Generated by Django 4.1.4 on 2022-12-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.IntegerField(max_length=20)),
                ('ligue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ligue')),
            ],
        ),
    ]
