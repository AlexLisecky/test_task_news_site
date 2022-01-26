from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views = models.IntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(max_length=500, verbose_name='Сообщение')

    def __str__(self):
        return self.text
