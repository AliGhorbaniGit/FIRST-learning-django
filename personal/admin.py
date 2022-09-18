from django.contrib import admin
from .models import ViewPersonal
# Register your models here.


class Pages(admin.ModelAdmin):

    list_display = ('author', 'status', )


admin.site.register(ViewPersonal, Pages)

