from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from kurstar.models import Course
import datetime


class StaticSitemapView(Sitemap):
    lastmod = datetime.datetime.now()
    i18n = True

    def items(self):
        return ['kurstar:index', 'kurstar:about']

    def location(self, obj):
        return reverse(obj)


class CoursesSitemapView(Sitemap):
    lastmod = datetime.datetime.now()
    i18n = True

    def items(self):
        return Course.objects.all()
