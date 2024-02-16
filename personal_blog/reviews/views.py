from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie_create.html"
    fields = [
        'movie_name', 
        'movie_year', 
        'movie_director', 
        'movie_rating',
        'movie_cover_image'
    ]
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movie_delete.html"    
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movie_update.html"
    fields = [
        'movie_name', 
        'movie_year', 
        'movie_director', 
        'movie_rating',
        'movie_cover_image'
    ]