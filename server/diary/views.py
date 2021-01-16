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
