# Generated by Django 4.0.1 on 2022-01-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0037_alter_theme_moduleformation_alter_theme_qe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consigne',
            name='pdf',
        ),
    ]