# Generated by Django 5.0.2 on 2024-05-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogretmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC', models.CharField(max_length=11)),
                ('AdiSoyadi', models.CharField(max_length=50)),
                ('Aciklama', models.CharField(max_length=255)),
            ],
        ),
    ]
