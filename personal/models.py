from statistics import mode
from django.db import models


# Create your models here.

class ViewPersonal(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    # image = models.ImageField(upload_to='images',max_length=1000)

    author = models.ForeignKey('auth.user', on_delete=models.CASCADE) # its cause when a user be deleted , everything

    # related to that user be deleted
    text = models.CharField(max_length=300)
    tt='ddd'
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.text
