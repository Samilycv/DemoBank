# Generated by Django 3.2.2 on 2023-02-20 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnkapp', '0004_auto_20230220_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnkapp.city'),
        ),
        migrations.AlterField(
            model_name='account',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnkapp.district'),
        ),
        migrations.AlterField(
            model_name='account',
            name='materials_provide',
            field=models.ManyToManyField(blank=True, to='bnkapp.MaterialsProvide'),
        ),
    ]