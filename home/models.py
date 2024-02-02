from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=30000)
    image = models.ImageField(upload_to='media/media/images', default='images/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    popular = models.BooleanField(default=False)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
