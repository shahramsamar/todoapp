# Generated by Django 4.2.11 on 2024-04-02 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_basicinformationmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicinformationmodel',
            options={'ordering': ['id']},
        ),
    ]