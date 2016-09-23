from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'To be constructed',
    }
    return render(request, 'home/index.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)