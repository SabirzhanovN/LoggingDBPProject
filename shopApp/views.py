from django.db import connection
from django.shortcuts import render
from .models import Product, LoggingMoves


def index(request):
    data = Product.objects.all()

    context = {'data': data}
    return render(request, 'shopApp/index.html', context)


def detail(request, id):
    data = Product.objects.get(id=id)

    context = {'data': data}
    return render(request, 'shopApp/detail.html', context)