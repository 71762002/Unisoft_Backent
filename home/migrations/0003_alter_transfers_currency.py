# Generated by Django 5.0.4 on 2024-04-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_transfers_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='currency',
            field=models.IntegerField(),
        ),
    ]