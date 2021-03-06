# Generated by Django 4.0.3 on 2022-04-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mungu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
