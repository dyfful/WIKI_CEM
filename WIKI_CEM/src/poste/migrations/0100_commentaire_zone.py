# Generated by Django 4.0.1 on 2022-05-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0099_delete_prioriter'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='Zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ZONE', to='poste.zone'),
        ),
    ]
