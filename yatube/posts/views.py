from django.http import HttpResponse, render


def index(request):
    return render(request, 'posts/index.html')


def group_posts(request, slug):
    return HttpResponse('лист')
