# Generated by Django 4.0.1 on 2022-01-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0024_client_poste'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='Groupement',
            field=models.ManyToManyField(to='poste.Groupement'),
        ),
    ]
