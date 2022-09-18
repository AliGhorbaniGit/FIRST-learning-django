from django.urls import path, include
from . import views
from pages.models import PageDetail

data = PageDetail.objects.all()

urlpatterns = [

    path('', views.ShowListView.as_view(), name='show_list', ),  # note that as_view given " () "
    path('add', views.Add.as_view(), name = 'add',),
    path('<int:pk>/', include('show.urls')),
    path('<int:pk>/update', views.UpadteView.as_view(), name='view_update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),
]
