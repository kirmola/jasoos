from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from .models import (
    Tool,
)
from django.urls import reverse


class ToolSitemap(Sitemap):

    def items(self):
        return Tool.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()
