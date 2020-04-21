# Generated by Django 3.0.5 on 2020-04-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlrequest',
            name='feedback',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='full_response',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='input_data',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='response',
            field=models.CharField(max_length=10000),
        ),
    ]
