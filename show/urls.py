from django.urls import path,include
from . import views
from show.models import Show
urlpatterns =[
    path('', views.ShowAllComment.as_view(),name='show_all_comment',),
    path('<int:pk>/',include('personal.urls')),
]
