from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=64, unique=True, verbose_name="Nom")

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"

    def __str__(self):
        return self.name

class Category(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True, verbose_name="Nom de la catégorie")
    description = models.CharField(max_length=255, blank=True, verbose_name="Description")
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Manga(models.Model):
   

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    volume = models.IntegerField(default=1, verbose_name="Volume")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Auteur")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    description = models.TextField(blank=True, verbose_name="Description")
    date = models.DateField(verbose_name="Date de publication")
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="ISBN")
    cover_image = models.ImageField(upload_to="mangas/", null=True, blank=True, verbose_name="Image de couverture")

    class Meta:
        verbose_name = "Manga"
        verbose_name_plural = "Mangas"
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-vol{self.volume}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - Vol {self.volume}"
