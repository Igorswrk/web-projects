# Generated by Django 5.0.2 on 2024-02-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_cover_image',
            field=models.ImageField(upload_to='./personal_blog/reviews/static/movies/media/<django.db.models.fields.CharField>.jpg'),
        ),
    ]
