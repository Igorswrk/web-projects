from django import forms

from .models import Movie, MovieReview 

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = [
            'movie_name', 
            'movie_year', 
            'movie_director', 
            'movie_rating',
            'movie_cover_image',
        ]
    

class MovieReviewFormSet(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = [
            'movie_rating',
            'movie_review_text',
            # 'movie_review_video'
        ]