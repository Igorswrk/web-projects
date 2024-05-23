from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
# from embed_video.fields import EmbedVideoField

class Movie(models.Model):

    movie_created_at = models.DateTimeField(auto_now_add=True)
    movie_updated_at = models.DateTimeField(auto_now=True)

    movie_name = models.CharField(max_length=100)
    movie_year = models.IntegerField()
    movie_director = models.CharField(max_length=100)
    movie_cover_image = models.ImageField(upload_to='movies/images/movies_covers/', null=True, blank=True)
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.movie_name
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"pk": self.pk})


class MovieReview(models.Model):
    review_created_at = models.DateTimeField(auto_now_add=True)
    review_updated_at = models.DateTimeField(auto_now=True)
    
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)
    movie_review_text = models.TextField()
    # movie_review_video = EmbedVideoField() # same like models.URLFields()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_review")

@receiver(post_delete, sender=Movie)
def delete_movie_image(sender, instance, **kwargs):
    if instance.movie_cover_image:
        instance.movie_cover_image.delete(save=False)