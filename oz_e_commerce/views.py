from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Oz42-Ecomm',
        'content': 'Bem vindo a Oz42'
    }
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        'title': 'Sobre',
        'content': 'Bem vindo a Oz42'
    }
    return render(request, 'about/view.html', context)


def contact_page(request):
    context = {
        'title': 'Página de contato',
        'content': 'Bem-vindo a página de contato'
    }
    return render(request, 'contact/view.html', context)
