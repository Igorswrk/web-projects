from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path("movies/", MovieListView.as_view(), name='movie_list'),
    path("movies/<int:pk>", MovieDetailView.as_view(), name='movie_detail'),
    # path("movies/add/", MovieCreateView.as_view(), name='movie_add'),      
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)