# Generated by Django 3.1 on 2022-06-21 23:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0119_auto_20220622_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='schemas_preferentiel',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
