from django.urls import path
from . import views

# Url Declaration movie_app
urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movies_detail'),
]
