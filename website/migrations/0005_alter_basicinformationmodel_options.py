# Generated by Django 4.2.11 on 2024-04-01 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_basicinformationmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicinformationmodel',
            options={'ordering': ['email', 'age']},
        ),
    ]
