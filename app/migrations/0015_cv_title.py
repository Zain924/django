# Generated by Django 4.2.4 on 2023-09-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_portfolio_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default='Default Title', max_length=20),
        ),
    ]
