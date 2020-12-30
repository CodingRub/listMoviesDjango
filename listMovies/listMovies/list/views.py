from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import Movies
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bs4 import BeautifulSoup
import requests

# Create your views here.
@login_required(login_url='login-page')
def home(request):
    query = request.GET.get("q")
    film = Movies.objects.all()
    mo = Movies.objects.all()
    annee = []
    genre = []
    genre2 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    if query:
        movie = film.filter(
            Q(title__icontains=query) |
            Q(date_released__icontains=query) |
            Q(synopsis__icontains=query) |
            Q(time__icontains=query) |
            Q(genre__icontains=query) |
            Q(author__icontains=query)
        )
    else:
        page = request.GET.get('page', 1)
        paginator = Paginator(film, 8)
        movie = paginator.page(page)
    l = []
    for i in film:
        a = i.date_released
        l.append(a.year)
    annee = list(set(l))

    for m in film:
        l2.append(m.genre)
    for i in l2:
        a = i.split(",")
        for elem in a:
            l3.append(elem)
    genre = list(set(l3))

    l4 = [b.genre for b in Movies.objects.all()]
    for g in l4:
        c = g.split(",")
        l5 = [q for q in c]
    genre2 = list(set(l5))

    movies = [p.title for p in Movies.objects.all()]
    print(movie)
    print(movies)
    movie2 = []
    rate = []
    name_rate = {}
    for m in movies:
        link_movie = m.replace(" ", "+")
        req = requests.get("https://www.imdb.com/find?q="+link_movie+"&ref_=nv_sr_sm")
        soup = BeautifulSoup(req.content, 'html.parser')
        for link in soup.find_all('td',attrs={"class":"result_text"}):
            a_tag = link.find("a")
            href=(a_tag.attrs['href'])
            if "/title/" in href:
                movie2.append(href)
                break
            print(href)
            print(film)

    for v in movie2:
        req = requests.get("https://www.imdb.com"+v)
        soup = BeautifulSoup(req.content, 'html.parser')
        for rating in soup.find_all('span', attrs={"itemprop":"ratingValue"}):
            rate.append(rating.text)

    total = zip(movie, rate)

    for m, r in total:
        name_rate[m] = r

    return render(request, 'list/home.html', {'movies': total, 'films': movie, 'years': annee, 'genre': genre, 'genre2': genre2})

def AtoZ(request):
    mov = Movies.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(mov, 8)
    movie = paginator.page(page)
    return render(request, 'list/AtoZ.html', {'movies': movie, 'title': 'A to Z:'})

@login_required(login_url='login-page')
def add(request):
    return render(request, 'list/add.html', {'title': 'Add Movies'})

def connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
        if user:
            login(request, user)
            return redirect('list-home')
        else:
            messages.warning(request, f"L'un des identifiants est faux !")
            return redirect('login-page')
    form = {}
    return render(request, 'list/login.html', form)

@login_required(login_url='login-page')   
def logoutUser(request):
    logout(request)
    return redirect('login-page')

@login_required(login_url='login-page') 
def delete_post(request, post_id):
    post = get_object_or_404(Movies, pk=post_id)
    post.delete()
    return redirect('dashboard-page')

@login_required(login_url='login-page')
def dashboard(request):
    if request.method == "POST":
        form = Movie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, f"Le film a bien été crée !")
            return redirect('dashboard-page')
            l = []
            l.append(form)
            print(l)
    else:
        form = Movie()
    return render(request, 'list/dashboard.html', {'title': 'Dashboard', 'form': form, 'movies': Movies.objects.all(), 'users': User.objects.all()})

