from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from diary.models import Article

# MTV
# Model, Template, View(python code)

# CRUD
# CR + L
# UD


def article_list(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        'articles': articles,
    }
    return render(request, 'diary/list.html', context)


def article_read(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'diary/read.html', context)


@csrf_exempt
def article_create(request):
    if request.method == 'GET':
        return render(request, 'diary/create.html')

    title = request.POST['title']
    content = request.POST['content']

    article = Article.objects.create(title=title, content=content)

    url = reverse('diary:article_read', kwargs={'pk': article.id})
    return redirect(url)


@csrf_exempt
def article_update(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(id=pk)
        context = {
            'article': article,
        }
        return render(request, 'diary/update.html', context)

    # POST
    title = request.POST['title']
    content = request.POST['content']

    Article.objects.filter(id=pk).update(title=title, content=content)

    url = reverse('diary:article_read', kwargs={'pk': pk})
    return redirect(url)


@csrf_exempt
def article_delete(request, pk):
    if request.method == 'GET':
        return redirect('/')

    # POST
    article = Article.objects.get(id=pk)
    article.delete()

    return redirect('/')
