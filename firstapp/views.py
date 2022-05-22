from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def page_not_found_view(request, exception):
    return HttpResponse("<h2>404 NOT FOUND</h2>Страница не найдена")


def index(request):
    data = {
        'service': range(1, 3)
    }
    context = {
        'header': 'Header'
    }
    return render(request, 'index.html', data)

