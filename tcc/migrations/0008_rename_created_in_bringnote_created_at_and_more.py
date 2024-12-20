# Generated by Django 5.1.1 on 2024-12-04 01:42

import django.utils.timezone
import tcc.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0007_bringnote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bringnote',
            old_name='created_in',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='bringnote',
            old_name='updated_in',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='create',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='create',
            name='task',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='register',
            name='cell',
            field=models.CharField(max_length=14, validators=[tcc.validators.invalid_cell]),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=100, validators=[tcc.validators.invalid_name]),
        ),
    ]
