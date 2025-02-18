# Generated by Django 5.1.3 on 2025-02-09 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Auteur',
                'verbose_name_plural': 'Auteurs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nom de la catégorie')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.RemoveField(
            model_name='livre',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='genre',
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('volume', models.IntegerField(default=1, verbose_name='Volume')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('date', models.DateField(verbose_name='Date de publication')),
                ('isbn', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='ISBN')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='mangas/', verbose_name='Image de couverture')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangalib.author', verbose_name='Auteur')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangalib.category', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Manga',
                'verbose_name_plural': 'Mangas',
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='Auteur',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Livre',
        ),
    ]
