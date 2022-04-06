from django.shortcuts import render

# Create your views here.

def grafica(request):
    return render(request, 'blog/grafica.html', {})

