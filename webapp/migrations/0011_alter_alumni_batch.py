# Generated by Django 4.1.4 on 2023-07-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alumni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='batch',
            field=models.IntegerField(),
        ),
    ]
