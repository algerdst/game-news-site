from django.shortcuts import render

from .models import Article, Category


def index(request, category_name=None):
    if category_name:
        category = Category.objects.get(name=category_name)
        articles = Article.objects.filter(category=category).order_by('-date')
    else:
        articles = Article.objects.all().order_by('-date')
    categories = Category.objects.all()
    popular_articles = Article.objects.filter(popular=True)
    data = {
        'categories': categories,
        'articles': articles,
        'popular_articles': popular_articles,
    }
    return render(request, 'home/index.html', context=data)


def article(request, slug_name):
    categories = Category.objects.all()
    article = Article.objects.get(slug=slug_name)
    popular_articles = Article.objects.filter(popular=True)
    article_category = article.category
    similar_posts = Article.objects.filter(category=article_category)[:3]
    data = {
        'categories': categories,
        'article': article,
        'popular_articles': popular_articles,
        'similar_posts': similar_posts
    }
    return render(request, 'home/article.html', context=data)
