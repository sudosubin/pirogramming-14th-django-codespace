from django.shortcuts import render

from diary.models import Article

# MTV
# Model, Template, View(python code)


def article_list(request):
    articles = Article.objects.all()
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
