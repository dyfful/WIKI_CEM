# Generated by Django 4.0.1 on 2022-04-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0081_alter_gmr_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerie',
            name='libelle',
            field=models.CharField(max_length=10),
        ),
    ]
