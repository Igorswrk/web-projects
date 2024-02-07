from django.db import models

class Movie(models.Model):

    movie_created_at = models.DateTimeField(auto_now_add=True)
    movie_updated_at = models.DateTimeField(auto_now=True)

    movie_name = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=100)
    movie_cover_image = models.ImageField(upload_to=f"personal_blog\\reviews\\static\\movies\\{self.movie_name}\\")
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.movie_name
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})

    