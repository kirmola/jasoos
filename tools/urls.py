from django.urls import path
from .views import (
    ToolsDetailView,
    HomePageListView,
)

urlpatterns = [
    path("", HomePageListView.as_view(), name="homepage"),
    path("<slug:tool_slug>/", ToolsDetailView.as_view(), name="Tool_detail"),
]
