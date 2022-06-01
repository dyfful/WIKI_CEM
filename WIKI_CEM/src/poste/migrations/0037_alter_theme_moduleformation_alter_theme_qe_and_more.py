# Generated by Django 4.0.1 on 2022-01-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0036_alter_formation_actualite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='ModuleFormation',
            field=models.CharField(max_length=40, verbose_name='Module de formation'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='QE',
            field=models.TextField(verbose_name='Quizz/Exercices'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='Theme',
            field=models.CharField(max_length=40, verbose_name='Thème'),
        ),
    ]
