# Generated by Django 4.0.1 on 2022-01-29 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_work_account'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='work',
            name='work_complete_id',
        ),
        migrations.RemoveIndex(
            model_name='work',
            name='work_type_complete_id',
        ),
    ]