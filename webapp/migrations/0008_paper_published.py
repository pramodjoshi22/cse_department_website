# Generated by Django 4.1.4 on 2023-07-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_research_cell_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper_published',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_names', models.CharField(max_length=700)),
                ('topic', models.CharField(max_length=500)),
                ('link', models.URLField(max_length=600)),
            ],
        ),
    ]
