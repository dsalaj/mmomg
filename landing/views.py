from django.shortcuts import render

# Create your views here.


def landing(request):
    context = {'test': 123}
    return render(request, 'landing/index.html', context)
