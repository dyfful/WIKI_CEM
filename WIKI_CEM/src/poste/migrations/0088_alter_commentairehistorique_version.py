# Generated by Django 4.0.1 on 2022-04-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0087_alter_commentairehistorique_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentairehistorique',
            name='Version',
            field=models.BigIntegerField(blank=True, default=0),
        ),
    ]
