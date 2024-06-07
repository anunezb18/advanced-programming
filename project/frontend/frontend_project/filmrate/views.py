from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Pelicula

def index(request):
    films_list = [
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/5.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "2",
            "image": "images/2.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "1",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "3",
            "image": "images/3.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "2",
            "image": "images/2.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/4.png"
        }
    ]
    return render(request, 'index.html', {"films": films_list})


def home(request):
    return render(request, 'home.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def create_account(request):
    return render(request, 'create_account.html')

def films(request):
    return render(request, 'films.html')

def films_user(request):
    return render(request, 'films_user.html')

def film(request):
    return render(request, 'film_template.html')

def my_watchlist(request):
    watchlist = [
        {
            "name": "Her",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/1.png"
        },
        {
            "name": "Joker",
            "description": "It's a movie of marvel studios",
            "stars": "4",
            "image": "images/2.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "1",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "3",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "2",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/1.png"
        }
    ]
    return render(request, 'my_watchlist.html', {"watchlist": watchlist})

def user(request):
    return render(request, 'user.html')

