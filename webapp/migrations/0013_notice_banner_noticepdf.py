# Generated by Django 4.1.4 on 2023-08-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_alumni_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='notices_images/')),
            ],
        ),
        migrations.CreateModel(
            name='NoticePdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='notices_pdf/')),
            ],
        ),
    ]
