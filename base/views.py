from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
# Create your views here.


def home(request, username):

    if not User.objects.filter(username=username).exists():
        return HttpResponseBadRequest('User "%s" does not exist.' % username)
    context = {'test': 123, 'username': username}
    return render(request, 'base/home.html', context)
