# Generated by Django 3.2.4 on 2021-06-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
