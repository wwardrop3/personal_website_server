# Generated by Django 4.1 on 2022-08-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalwebsiteapi', '0006_membermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='formmodel',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='personalwebsiteapi.membermodel'),
            preserve_default=False,
        ),
    ]
