# Generated by Django 4.0.1 on 2022-04-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0095_remove_commentaire_historique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=15)),
            ],
        ),
    ]