from django.urls import path

from .views import IndexView, NewsView, ContactView, AboutView, FeedbackView

app_name = 'news_main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', NewsView.as_view(), name='news'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
