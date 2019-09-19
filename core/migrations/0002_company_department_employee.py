# Generated by Django 2.2.5 on 2019-09-19 10:13

import core.db.fields
import core.db.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', core.db.fields.ShardIDField(help_text='Unique Shard ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Company name', max_length=255)),
                ('slug', models.SlugField(blank=True, help_text='Company slug')),
                ('founded_at', models.CharField(blank=True, help_text='Company founded year', max_length=4, null=True, validators=[core.db.validators.year_validator])),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', core.db.fields.ShardIDField(help_text='Unique Shard ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Department name', max_length=255)),
                ('slug', models.SlugField(blank=True, help_text='Department slug')),
                ('company', models.ForeignKey(help_text='Department company', on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', core.db.fields.ShardIDField(help_text='Unique Shard ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='First name', max_length=255)),
                ('last_name', models.CharField(help_text='First name', max_length=255)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('undefined', 'undefined')], default='undefined', max_length=10)),
                ('active', models.BooleanField(default=True, help_text='Active Employee')),
                ('company', models.ForeignKey(help_text='Company', on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
                ('department', models.ForeignKey(help_text='Department', on_delete=django.db.models.deletion.CASCADE, to='core.Department')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
