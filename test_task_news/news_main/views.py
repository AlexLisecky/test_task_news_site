from django.shortcuts import render
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'news_main/index.html'
    queryset = []


class NewsView(ListView):
    pass


class ContactView(ListView):
    pass


class AboutView(ListView):
    pass


class FeedbackView(ListView):
    pass
