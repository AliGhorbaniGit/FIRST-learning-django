from django.contrib import admin
from .models import Show

# Register your models here.


class ShowAdmin(admin.ModelAdmin):
    list_display = ('akkk',)


admin.site.register(Show)
