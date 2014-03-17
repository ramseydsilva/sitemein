from django.contrib import admin
from .models import *


class SiteRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(SiteRequest, SiteRequestAdmin)
