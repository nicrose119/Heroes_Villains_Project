# Generated by Django 4.1.5 on 2023-01-12 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0003_rename_super_supers'),
    ]

    operations = [
        migrations.AddField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.super_types'),
        ),
    ]
