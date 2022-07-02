from django.urls import path
from .views import MovieListView, MovieCreateView, MovieDetailView, MovieFavoriteView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/favorite/', MovieFavoriteView.as_view(), name='movie-favorite'),
]
