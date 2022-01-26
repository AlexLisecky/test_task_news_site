from django.shortcuts import render
from django.views.generic import ListView

from .models import News, Comment


class IndexView(ListView):
    template_name = 'news_main/index.html'
    model = News
    queryset = News.objects.all()[:5]


class NewsView(ListView):
    template_name = 'news_main/news.html'
    queryset = []


class ContactView(ListView):
    template_name = 'news_main/contacts.html'
    queryset = []


class AboutView(ListView):
    template_name = 'news_main/about.html'
    queryset = []


class FeedbackView(ListView):
    template_name = 'news_main/feedback.html'
    queryset = []
