from rest_framework import serializers
from .models import Author, Manga, Category



class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id','title','author','category','description','cover_image']
    # def get_photo_url(self,obj):
        # request = self.context.get('request')
        # photo_url = obj.fingerprint.url


class AuthorListSerializer(serializers.ModelSerializer):

    # mangas = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = '__all__'
    

class AuthorDetailSerializer(serializers.ModelSerializer):

    mangas = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = '__all__'
    
    def get_mangas(self,instance):
        queryset = instance.mangas.all()
        serializer = MangaListSerializer(queryset,many=True)
        return serializer.data
    

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    mangas = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_mangas(self, instance):
        queryset = instance.mangas.all()
        serializer = MangaListSerializer(queryset, many=True)
        return serializer.data