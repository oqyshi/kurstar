from django.urls import path

from . import views

app_name = 'seo'
urlpatterns = [
    path('robots.txt', views.RobotsView.as_view(), name='robots'),
]
