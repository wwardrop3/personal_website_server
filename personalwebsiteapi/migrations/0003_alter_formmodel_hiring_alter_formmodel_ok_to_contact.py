# Generated by Django 4.1 on 2022-08-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalwebsiteapi', '0002_alter_formmodel_hiring_alter_formmodel_ok_to_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='hiring',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ok_to_contact',
            field=models.BooleanField(),
        ),
    ]
