from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, ListView
from .models import Tool

class ToolsDetailView(DetailView):
    model = Tool
    slug_url_kwarg = "tool_slug"
    slug_field = "tool_slug"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        current_tool = self.kwargs.get("tool_slug")
        match current_tool:
            case "username-osint":
                template_name = "tools/username-osint.html"
            case "encoding-osint":
                template_name = "tools/encoding-osint.html"
            case "decoding-osint":
                template_name = "tools/decoding-osint.html"
            case "documentation-osint":
                template_name = "tools/documentation-osint.html"
            case "domain-name-osint":
                template_name = "tools/domain-name-osint.html"
            case "email-address-osint":
                template_name = "tools/email-address-osint.html"
            case "interpol-osint":
                template_name = "tools/interpol-osint.html"
            case "ip-address-osint":
                template_name = "tools/ip-address-osint.html"
            case "map-osint":
                template_name = "tools/map-osint.html"
            case "search-engine-osint":
                template_name = "tools/search-engine-osint.html"
            case "telephone-osint":
                template_name = "tools/telephone-osint.html"
        self.template_name = template_name
        return super().get(request, *args, **kwargs)

    
    

class HomePageListView(ListView):
    model = Tool
    template_name = "tools/tools_list.html"

    def get_queryset(self):
        return super().get_queryset().all()
    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["all_tools"] = self.get_queryset()
        return context
    