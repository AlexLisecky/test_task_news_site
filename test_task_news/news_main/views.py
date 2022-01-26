from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView

from .models import News


class IndexView(ListView):
    """ Главная страница"""
    template_name = 'index.html'
    model = News
    queryset = News.objects.all().order_by('-views')[:5]
    context_object_name = 'news'


class NewsView(ListView):
    """ Страница новостей"""
    template_name = 'news_main/news.html'
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'


class ContactView(ListView):
    """ Страница контактов """
    template_name = 'news_main/contacts.html'
    queryset = []


class AboutView(ListView):
    """ Страница о нас """
    template_name = 'news_main/about.html'
    queryset = []


class FeedbackView(ListView):
    """ Страница обратной связи """
    template_name = 'news_main/feedback.html'
    queryset = []


class NewsCreateView(CreateView):
    """ Создание новой новости """
    model = News
    template_name = 'news_main/add_news.html'
    success_url = '/'
    fields = ['title', 'description']


class NewsUpdateView(UpdateView):
    """ Редактирование новости """
    model = News
    template_name = 'news_main/update_news.html'
    success_url = '/'
    fields = ['title', 'description']


def delete_view(request, pk):
    """ Удаление новости """
    context = {}
    obj = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "news_main/delete_view.html", context)
