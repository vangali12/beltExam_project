# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='from_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to='loginReg_app.User'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='to_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to='loginReg_app.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='relationships',
            field=models.ManyToManyField(related_name='_user_relationships_+', through='loginReg_app.Relationship', to='loginReg_app.User'),
        ),
    ]