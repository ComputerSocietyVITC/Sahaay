# Generated by Django 3.2.9 on 2021-11-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentstable',
            name='uniqueID',
            field=models.CharField(blank=True, default='000VITCC---', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='issues',
            name='uniqueID',
            field=models.CharField(blank=True, default='000VITCC---', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='issues',
            name='Date_of_Creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='issues',
            name='Department',
            field=models.CharField(blank=True, choices=[['ADM', 'Administrator'], ['MGM', 'Management']], default='Admin', max_length=200),
        ),
    ]
