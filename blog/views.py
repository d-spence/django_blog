from django.shortcuts import render
from django.http import HttpResponse

# Dummy data
posts = [
    {
        'author': 'Dan Spencer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 10, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 11, 2020'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)