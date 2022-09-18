from django.urls import path
from . import views
urlpatterns = [
    path('',views.person_show,name='person_show'),
]