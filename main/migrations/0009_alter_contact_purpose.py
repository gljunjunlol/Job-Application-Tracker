# Generated by Django 3.2.4 on 2021-06-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210625_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='purpose',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('IS', 'Internship'), ('C', 'Contract'), ('F', 'Freelancer'), ('T', 'Temporary'), ('TR', 'Trainee')], max_length=2),
        ),
    ]
