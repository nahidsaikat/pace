from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, View
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .filters import MovieFilter
from .forms import MovieForm
from .models import Movie
from .tables import MovieTable


class MovieListView(SingleTableMixin, FilterView):
    table_class = MovieTable
    model = Movie
    template_name = "movies/movie_list.html"
    filterset_class = MovieFilter

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['favorite_movie_list'] = self.object_list.filter(my_favorite=True)
        return data


class MovieCreateView(View):
    queryset = Movie.objects.all()
    form_class = MovieForm
    template_name = 'movies/movie_create.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/')

        return render(request, self.template_name, {'form': form})


class MovieDetailView(DetailView):
    queryset = Movie.objects.all()
    template_name = 'movies/movie_details.html'


class MovieFavoriteView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.my_favorite = True
        movie.save()
        return redirect(reverse('movie-detail', args=[movie.id]))
