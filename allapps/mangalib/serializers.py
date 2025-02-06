from rest_framework import serializers
from .models import Auteur,Livre,Categorie

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'
    # def get_photo_url(self,obj):
        # request = self.context.get('request')
        # photo_url = obj.fingerprint.url

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fieds = '__all__'