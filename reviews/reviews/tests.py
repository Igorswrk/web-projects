from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from .models import Movie

class MovieModelTest(TestCase):
    
    def setUp(self):
        self.movie = Movie.objects.create(
            movie_name='Avengers - Endgame',
            movie_year= 2019,
            movie_director='Anthony Russo, Joe Russo',
            movie_rating=10.0,
            movie_cover_image = '\movies\images\movies_covers\1f8373201516a4657649d61e97b1f91a_WhvCLCe.jpg'            
        )
    
    def test_movie_get_absolute_url(self):
        self.assertEqual(self.movie.get_absolute_url(), reverse('movie_detail', kwargs={'pk': 1}))

    def test_movie_created_at(self):
        # Verifica se a data de criação foi atribuída automaticamente
        self.assertTrue(isinstance(self.movie.movie_created_at, datetime))

    def test_movie_updated_at(self):
        # Verifica se a data de atualização é a mesma que a de criação após a criação do filme
        self.assertEqual(self.movie.movie_created_at, self.movie.movie_updated_at)
        
        # Altera algo no filme
        self.movie.movie_rating = 9.0
        self.movie.movie_updated_at = datetime.now()
        
        # Verifica se a data de atualização foi atualizada após a alteração
        self.assertNotEqual(self.movie.movie_created_at, self.movie.movie_updated_at)
    
    def test_movie_movie_name_content(self):
        self.assertEqual(self.movie.movie_name, 'Avengers - Endgame')
    
    def test_movie_movie_year_content(self):
        self.assertEqual(self.movie.movie_year,2019)
    
    def test_movie_movie_director_content(self):
        self.assertEqual(self.movie.movie_director, 'Anthony Russo, Joe Russo')
    
    def test_movie_movie_rating_content(self):
        self.assertEqual(self.movie.movie_rating, 10.0)
    
    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_list.html')
        self.assertIn('<Movie: Avengers - Endgame>', str(response.context))
        
    def test_movie_detail_view(self):
        response = self.client.get(reverse('movie_detail', kwargs={'pk': self.movie.pk}))
        no_response = self.client.get(reverse('movie_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'movie_detail.html')
        self.assertIn('<Movie: Avengers - Endgame>', str(response.context))
    
    def test_movie_create_view(self):
        movie_test = {
            'movie_name'       :'New movie',
            'movie_year'       : 2019,
            'movie_director'   : 'New Director',
            'movie_rating'     : 10.0,
            'movie_cover_image': '\movies\images\movies_covers\1f8373201516a4657649d61e97b1f91a_WhvCLCe.jpg'
        }
    
        response = self.client.post(reverse('movie_create'), data=movie_test)
        self.assertEqual(response.status_code, 302)  # Verifica se o status code é 302 (redirecionamento temporário)
        self.assertEqual(response.url, reverse('movie_list'))  # Verifica se o redirecionamento é para a lista de filmes

    def test_movie_update_view(self):
        
        movie_test = Movie.objects.create(
            movie_name='Avengers - Infinity war',
            movie_year= 2019,
            movie_director='Anthony Russo, Joe Russo',
            movie_rating=10.0,
            movie_cover_image = '\movies\images\movies_covers\1f8373201516a4657649d61e97b1f91a_WhvCLCe.jpg'            
        )

        movie_update = {
            'movie_name'       :'Title Updated',
            'movie_director'   :'New Director',
        }

        response = self.client.post(
            reverse('movie_update', kwargs={'pk': movie_test.pk}), 
            data=movie_update
        )

        self.assertEqual(response.status_code, 302) 

        self.assertIn('<Movie: Title Updated>', str(response.context))
        self.assertIsNot('<Movie: Avengers - Infinity war>', str(response.context))
    
        movie_test.refresh_from_db()

    def test_movie_delete_view(self):
        movie_test = self.client.create(
            movie_name='Avengers - Infinity war',
            movie_year= 2019,
            movie_director='Anthony Russo, Joe Russo',
            movie_rating=10.0,
            movie_cover_image = '\movies\images\movies_covers\1f8373201516a4657649d61e97b1f91a_WhvCLCe.jpg'            
        )
        
        response = self.client.post(
            reverse('post_delete', kwargs={'pk': movie_test.pk})
        )

        self.assertEqual(response.status_code, 302)