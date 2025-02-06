from django.db import models

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length=64, unique = True,verbose_name="Nom")
    class Meta:
        verbose_name ="Auteur"
        verbose_name_plural ="Auteurs"
    def __str__(self):
        return self.nom

class Categorie(models.Model):

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=65)    

    def __str__(self):
        return self.name


class Livre(models.Model):
    titre = models.CharField(max_length = 32, unique=True,verbose_name="Titre")
    quantity = models.IntegerField(default=1,verbose_name="Quantité")
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE,verbose_name="Auteur")
    date = models.DateField(verbose_name="Date de diffusion")
    image_profile = models.ImageField(verbose_name="Image d'affiche",upload_to="images/",null=True)
    genre = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    class Meta:
        verbose_name ="Livre"
        verbose_name_plural ="Livres"
    def __str__(self):
        return self.titre


 

