from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView

from .models import News, Comment


class IndexView(ListView):
    template_name = 'index.html'
    model = News
    queryset = News.objects.all().order_by('-views')[:5]
    context_object_name = 'news'


class NewsView(ListView):
    template_name = 'news_main/news.html'
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'


class ContactView(ListView):
    template_name = 'news_main/contacts.html'
    queryset = []


class AboutView(ListView):
    template_name = 'news_main/about.html'
    queryset = []


class FeedbackView(ListView):
    template_name = 'news_main/feedback.html'
    queryset = []


class NewsCreateView(CreateView):
    model = News
    template_name = 'news_main/add_news.html'
    success_url = '/'
    fields = ['title', 'description']


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news_main/update_news.html'
    success_url = '/'
    fields = ['title', 'description']


def delete_view(request, pk):
    context = {}
    obj = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "news_main/delete_view.html", context)