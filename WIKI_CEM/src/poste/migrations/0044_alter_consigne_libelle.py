# Generated by Django 4.0.1 on 2022-01-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0043_alter_categorieconsigne_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consigne',
            name='libelle',
            field=models.CharField(max_length=100),
        ),
    ]
