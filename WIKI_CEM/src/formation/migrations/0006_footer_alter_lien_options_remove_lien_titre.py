# Generated by Django 4.0.1 on 2022-05-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0005_alter_lien_options_rename_libelle_lien_titre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Titre pied de page',
                'ordering': ['Titre'],
            },
        ),
        migrations.AlterModelOptions(
            name='lien',
            options={'ordering': ['nom'], 'verbose_name': 'Lien utile'},
        ),
        migrations.RemoveField(
            model_name='lien',
            name='Titre',
        ),
    ]
