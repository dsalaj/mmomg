from django.shortcuts import render

# Create your views here.


def landing(request):
    context = {'auth': request.user.is_authenticated}
    return render(request, 'landing/index.html', context)
