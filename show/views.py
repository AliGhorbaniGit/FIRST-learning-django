from django.shortcuts import render
from .models import Show
from pages.models import PageDetail
from personal.models import ViewPersonal
# if i want to write a eception without model's name , i must import this :
from django.core.exceptions import ObjectDoesNotExist
# and then replace row 14 by this code : except ObjectDoesNotExist
from django.views import generic

# OR we can replace there 👇 :
# try:
#         data = PageDetail.objects.get(pk=pk)
#     except PageDetail.DoesNotExist :
#         print("not found")
#         data=None
#
# by this code :
# first import :
# from django.shortcuts import get_object_or_404  AND THEN
# replace those cod with this : data = get_object_or_404(PageDetail,pk)



# def show_all_comment(request, pk):
#
#     try:
#         pd = ViewPersonal.objects.filter(status='pub')
#         data = PageDetail.objects.get(pk=pk)
#
#     except PageDetail.DoesNotExist :
#         print("not found")
#         data = None
#     return render(request, 'show/_base.html', {'person': pd, 'datas': data})


class ShowAllComment(generic.DetailView):
    model = PageDetail
    context_object_name = 'person'
    template_name = 'show/_base.html'

