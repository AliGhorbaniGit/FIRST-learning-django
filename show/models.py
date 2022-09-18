from statistics import mode
from django.db import models
from pages.models import PageDetail
from personal.models import ViewPersonal

# Create your models here.

class Show(models.Model):
  #  image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

