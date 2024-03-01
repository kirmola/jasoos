from django.urls import path
from .views import (
    ToolsDetailView
)

urlpatterns = [
    path("<slug:tool_slug>/", ToolsDetailView.as_view(), name="tools_name")
]
