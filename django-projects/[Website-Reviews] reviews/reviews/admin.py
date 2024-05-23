from django.contrib import admin
from .models import Movie, MovieReview

class MovieReviewInline(admin.StackedInline):
    model = MovieReview
    readonly_fields = (
        'review_created_at',
        'review_updated_at',
    )
    extra = 1   
    show_change_link = True


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieReviewInline]
