from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    # db에 전체 데이터 조회 
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.GET.get('title')
    audience = request.GET.get('audience')
    release_date = request.GET.get('release_date')
    genre = request.GET.get('genre')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    
    