# Generated by Django 4.1.4 on 2022-12-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='id',
        ),
        migrations.AddField(
            model_name='match',
            name='id_match',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
