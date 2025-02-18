# Generated by Django 5.1.3 on 2025-02-06 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64, unique=True, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Auteur',
                'verbose_name_plural': 'Auteurs',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=32, unique=True, verbose_name='Titre')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantité')),
                ('date', models.DateField(verbose_name='Date de diffusion')),
                ('image_profile', models.ImageField(null=True, upload_to='images/', verbose_name="Image d'affiche")),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangalib.auteur', verbose_name='Auteur')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangalib.categorie')),
            ],
            options={
                'verbose_name': 'Livre',
                'verbose_name_plural': 'Livres',
            },
        ),
    ]
