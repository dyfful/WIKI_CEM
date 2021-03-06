# Generated by Django 4.0.1 on 2022-04-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0090_remove_commentairehistorique_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentaire',
            options={'ordering': ['-DateCreation']},
        ),
        migrations.RenameField(
            model_name='commentaire',
            old_name='Date',
            new_name='DateModification',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='DateCreation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='Nom',
            field=models.CharField(max_length=55, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='Prenom',
            field=models.CharField(max_length=55, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='commentairehistorique',
            name='Action',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='commentairehistorique',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentairehistorique',
            name='DateAction',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
