from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

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
        

@receiver(post_delete, sender=Movie)
def delete_movie_image(sender, instance, **kwargs):
    if instance.movie_cover_image:
        instance.movie_cover_image.delete(save=False)

    

