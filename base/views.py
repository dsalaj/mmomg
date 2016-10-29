from django.shortcuts import render

# Create your views here.


def home(request, username):
    context = {'test': 123, 'username': username}
    return render(request, 'base/home.html', context)
