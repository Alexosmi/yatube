from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'text': "Это главная страница проекта Yatube"
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    context = {
        'text': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, slug, context)
