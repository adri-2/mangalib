from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import AuthorListSerializer,CategoryListSerializer,MangaListSerializer,AuthorDetailSerializer,CategoryDetailSerializer
from .models import Author, Manga, Category
from .permissions import IsAdminAuthenticated
from rest_framework.decorators import api_view


# Create your views here.
class AuthorViewset(ReadOnlyModelViewSet):
   
    serializer_class=AuthorListSerializer
    detail_serializer_class=AuthorDetailSerializer

    def get_queryset(self):
        return Author.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer

    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
       


class MangaViewset(ReadOnlyModelViewSet):

    serializer_class = MangaListSerializer
    queryset = Manga.objects.all()

    # def get_queryset(self):

    #     queryset = Manga.objects.all()
    #     author_id = self.request.GET.get('author_id')
    #     if author_id is not None:
    #         queryset = queryset.filter(author_id=author_id)
    #     return queryset

class AdminMangaViewset(ModelViewSet):

    serializer_class = MangaListSerializer

    queryset = Manga.objects.all()

    permission_classes = [IsAdminAuthenticated]
      



def index_view(request):
    return render(request, "dist/index.html", {})



@api_view(['GET'])
def allBooks(request):
    livres = Manga.objects.all()
    serialization =MangaListSerializer(livres,many=True)
    return Response(serialization.data)


# @api_view(['GET'])
# def showBooks(request,livre_id): 
#     livre =  Livre.objects.get(pk=livre_id)
#     serializer = LivreSerializer(livre)
#     return Response(serializer.data)


# @api_view(['POST'])
# def addBooks(request):
#     serializer = LivreSerializer(data = request.data,many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def updateBook(request,id):
#     book = Livre.objects.get(id=id)
#     serializer = LivreSerializer(instance=book,date=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def delBook(request,id):
#     book=Livre.objects.get(id=id)
#     book.delete()
#     return Response('Livre supprime !!')

# @api_view(['POST'])
# def addAuthor(request):
#     serializer = AuteurSerializer(data = request.data,many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def addCategory(request):
#     serializer = CategorieSerializer(data = request.data,many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def index(request):
#     context = {
#        "livres": livre.objects.all() }
#     return render(request,"mangalib/index.html",context)
    # """
    # if request.method == 'POSt':
    #     form = SomeFrom(request.POST)

    #     if form.is_valid ():
    #         return redirect("mangalib:index")
    # else:
    #     form = SomeFrom()
    # context = { "form": form}
    # return render(request,"mangalib/index.html",context)
    # """

# def show(request,livre_id): 
#     context = {"livre": get_list_or_404(livre,pk=livre_id),
               
#             }
#     return render(request, "mangalib/show.html", context)


# def add_livre(request):
#     #auteurs = Auteur.objects.get(nom= "Akira Toriyama" )
#     #livres = livre.objects.create(titre = "Dragon Ball Z", quantity=4,auteur=auteurs)
#     #livres = livre.objects.create(titre = "Dragon Ball", quantity=4,auteur=auteurs)
#     #livres = livre.objects.create(titre = "Dragon Ball GT", quantity=4,auteur=auteurs)
#     if request.method == 'POST':
#         form = LivreForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("mangalib:index")
#     else:
#         form = LivreForm()
#     context = {"form": form}
#     return render(request,"mangalib/livre-form.html",context)

# def edit_livre(request,livre_id):
#     livres = livre.objects.get(pk=livre_id)
#     if request.method == 'POST':
#         form = LivreForm(request.POST,instance=livres)
#         if form.is_valid():
#             form.save()
#             return redirect("mangalib:index")
#     else:
#         form = LivreForm(instance=livres)
#     return render(request,"mangalib/livre-form.html",{"form": form})


# def del_livre(request,livre_id):
#     book = livre.objects.get(pk=livre_id)
#     book.delete()
#     return redirect("mangalib:index")
