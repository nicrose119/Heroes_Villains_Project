# Generated by Django 4.1.5 on 2023-01-12 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0004_supers_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='super_types.super_types'),
            preserve_default=False,
        ),
    ]