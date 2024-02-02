from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("<str:category_name>", views.index, name='category'),
    path("article/<slug:slug_name>", views.article, name='article'),
]
