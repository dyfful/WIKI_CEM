# Generated by Django 4.0.1 on 2022-04-25 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0094_commentaire_historique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='Historique',
        ),
    ]
