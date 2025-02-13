from django.contrib import admin
from .models import Author, Category, Manga

# Configuration de l'administration pour les auteurs
@admin.register(Author)  
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Correction de 'nom' en 'name'
    search_fields = ('name',)

# Configuration de l'administration pour les mangas
@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Correction des champs
    list_filter = ('author', 'category')  # Ajout du filtre par catégorie et statut
    search_fields = ('title', 'author__name')  # Permet de rechercher un auteur par son nom
    prepopulated_fields = {'slug': ('title',)}  # Génération automatique du slug

# Configuration de l'administration pour les catégories
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Génération automatique du slug



#mais il est mis ici sur <1>
