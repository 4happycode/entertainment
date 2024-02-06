from django.shortcuts import render
from .models import Movies


# List Of Movies
def movies(request):
    movie = Movies.objects.all()
    return render(request, 'movie_list.html', {'movies': movie})


# Detail Of Movies
def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})
