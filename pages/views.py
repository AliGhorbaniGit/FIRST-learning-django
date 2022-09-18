from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewAutoModel
from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import reverse
from django.urls import reverse_lazy

# my import
from .models import PageDetail
from . import urls


# Create your views here.


# def show_list_veiw(request):
#     m = PageDetail.objects.all()  # i can sort the page by : .order_by('dataCreated') if wanna to sort revers(means assend)
#    # just need to add ' - ' to code like this :.order_by('-dataCreated')
#
#     return render(request, 'pages/show_list.html', {'show_list': m})

# instead uper functional code i use following code as class_based_view :

class ShowListView(generic.ListView):
    model = PageDetail
    template_name = 'pages/show_list.html'
    context_object_name = 'show_list'
    # if i wanna set a filter on my query_set i must use than : following cod instead of "  model = PageDetail "
    # def get_queryset(self):
    #   return PageDetail.objects.filter(status='pub')


# def add(request):
#     if request.method == 'POST':
#         form = NewAutoModel(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show_list')
#
#     else:  # Get Request
#         form = NewAutoModel()
#     return render(request, 'pages/add.html', context={'form': form}, )
#


class Add(generic.CreateView):
    form_class = NewAutoModel
    template_name = 'pages/add.html'


# def view_update(request, pk):
#     post = get_object_or_404(PageDetail, pk=pk)
#     form = NewAutoModel(request.POST or None, instance=post)
#
#     if form.is_valid():
#         print('ali')
#         form.save()
#         return redirect('show_list')
#
#     return render(request, 'pages/add.html', context={'form': form})


class UpadteView(generic.UpdateView):
    template_name = 'pages/add.html'
    form_class = NewAutoModel
    model = PageDetail


# def delete(request, pk):
#     post = get_object_or_404(PageDetail, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         print("ahhhh")
#         return redirect('show_list')
#     return render(request,'pages/delete.html',context={'post':post})


class Delete(generic.DeleteView):
    model = PageDetail
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('show_list')  # i can use following code insteed of this
#   def get_success_url(self):
#      reverse('show_list')
