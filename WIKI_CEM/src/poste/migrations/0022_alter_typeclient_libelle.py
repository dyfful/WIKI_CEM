# Generated by Django 4.0.1 on 2022-01-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0021_typeclient_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeclient',
            name='libelle',
            field=models.CharField(max_length=20),
        ),
    ]
