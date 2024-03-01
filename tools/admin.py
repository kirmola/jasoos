from django.contrib import admin
from .models import (
    Tool,
)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass
