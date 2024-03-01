from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Tool(models.Model):

    tool_name = models.CharField(_("Tool Name"), max_length=50)
    tool_slug = AutoSlugField(populate_from="tool_name")
    # tool_icon = models.ImageField(_("Icon"), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Tool")
        verbose_name_plural = _("Tools")

    def __str__(self):
        return self.tool_name

    def get_absolute_url(self):
        return reverse("Tool_detail", kwargs={"tool_slug": self.tool_slug})

