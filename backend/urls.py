"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from allapps.mangalib.views import MangaViewset, AuthorViewset,CategoryViewset,index_view,AdminMangaViewset
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('author',AuthorViewset,basename='author')
router.register('manga',MangaViewset,basename='manga')
router.register('category',CategoryViewset,basename='category')
router.register('admin/manga',AdminMangaViewset,basename='admin-manga')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('allapps.mangalib.urls')),
    path("",index_view, name="index"),
    path('api/',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
