from django.urls import path
from . import views

urlpatterns = [
    path('sinin/',views.CreateUser.as_view(),name='createuser'),
]