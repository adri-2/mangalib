from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('libre',views.LivreViewset)
app_name = "mangalib"

# urlpatterns = [
#     path('',views.index, name='index'),  # manga/
#     path('<int:livre_id>/',views.show,name= 'show'),   # manga/<id>
#     path('ajouter_livre/',views.add_livre,name='add_livre'),
#     path('modifie_livre/<int:livre_id>/',views.edit_livre,name='edit_livre'),
#     path('suprime_livre/<int:livre_id>/',views.del_livre,name='del_livre'),
# ]

# urlpatterns = [
#     path('livre/', include(router.urls)), 
# ]

urlpatterns = [
      path("", views.index_view, name="index"),
        # livre
    path('livre/', views.allBooks), 
    path('livre/<int:livre_id>/',views.showBooks), 
    path('addBooks/',views.addBooks),
    path('livre/update/<int:id>/',views.updateBook),
    path('livre/delete/<int:id>/',views.delBook),
    # auteur
    path('author/add/',views.addAuthor),
    # path('author/update/<int:id>/',views.updateAuthor),
    # path('author/delete/<int:id>/',views.dellAuthor),

    # categorie
     path('category/add/',views.addCategory),
    # path('category/update/<int:id>/',views.updateCategory),
    # path('category/delete/<int:id>/',views.dellCategory),

    # url vuejs
     path("static/livres/", views.index_view, name="index"),
         path("static/about/", views.index_view, name="index"),
         path("static/", views.index_view, name="index"),
        #  path("", views.index_view, name="index"),
]