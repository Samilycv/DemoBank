# Generated by Django 3.2.2 on 2023-02-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnkapp', '0003_auto_20230220_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='materials_provide',
        ),
        migrations.AddField(
            model_name='account',
            name='materials_provide',
            field=models.ManyToManyField(to='bnkapp.MaterialsProvide'),
        ),
    ]
