from django.shortcuts import render
from django.views.generic import DetailView, TemplateView


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
