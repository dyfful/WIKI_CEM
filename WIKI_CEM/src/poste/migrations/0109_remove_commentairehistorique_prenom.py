# Generated by Django 4.0.1 on 2022-05-18 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0108_remove_commentaire_prenom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentairehistorique',
            name='Prenom',
        ),
    ]
