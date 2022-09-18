from statistics import mode
from django.db import models
from django.shortcuts import reverse


# it's for main page of website

class PageDetail(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_list')
