from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User  # default Django User model

# Create your views here.

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')


def users_list(request):
    users = User.objects.all()
    return render(request, 'pages/users.html', {
        'users': users,
        'segment': 'users'
    })
