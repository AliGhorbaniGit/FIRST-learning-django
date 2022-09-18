from django.contrib import admin
from .models import PageDetail
# Register your models here.


class Pages(admin.ModelAdmin):

    list_display = ('title', 'text', )


admin.site.register(PageDetail, Pages)  # its equal to @admin.register((PageDetail))


