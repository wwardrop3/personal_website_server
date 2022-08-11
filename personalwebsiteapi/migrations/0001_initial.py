# Generated by Django 4.1 on 2022-08-10 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('company', models.TextField()),
                ('ok_to_contact', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndustryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FormSkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwebsiteapi.formmodel')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwebsiteapi.skillmodel')),
            ],
        ),
        migrations.AddField(
            model_name='formmodel',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwebsiteapi.industrymodel'),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
