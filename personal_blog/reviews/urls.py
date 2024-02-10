from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import (
    MovieListView, 
    MovieDetailView, 
    MovieCreateView, 
    MovieDeleteView,
    MovieUpdateView
)

urlpatterns = [
    path("movies/", MovieListView.as_view(), name='movie_list'),
    path("movies/<int:pk>", MovieDetailView.as_view(), name='movie_detail'),
    path("movies/create/", MovieCreateView.as_view(), name='movie_create'),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name='movie_delete'),
    path("movie/<int:pk>/update/", MovieUpdateView.as_view(), name="movie_update"),      
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)