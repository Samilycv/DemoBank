# Generated by Django 3.2.2 on 2023-02-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnkapp', '0002_auto_20230220_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialsProvide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')], max_length=50),
        ),
    ]
