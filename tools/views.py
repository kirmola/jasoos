from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import DetailView
from .models import Tool

class ToolsDetailView(DetailView):
    model = Tool
    template_name = "tools/tools_list.html"
    slug_url_kwarg = "tool_slug"
    slug_field = "tool_slug"
    context_object_name = "tool"

