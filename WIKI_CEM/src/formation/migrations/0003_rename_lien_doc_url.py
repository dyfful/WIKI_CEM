# Generated by Django 4.0.1 on 2022-05-30 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_alter_doc_lien'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc',
            old_name='lien',
            new_name='url',
        ),
    ]
