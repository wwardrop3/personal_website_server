# Generated by Django 4.1 on 2022-08-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalwebsiteapi', '0003_alter_formmodel_hiring_alter_formmodel_ok_to_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodel',
            name='skills',
            field=models.ManyToManyField(related_name='form', through='personalwebsiteapi.FormSkillModel', to='personalwebsiteapi.skillmodel'),
        ),
    ]
