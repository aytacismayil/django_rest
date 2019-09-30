from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import NewSerializer ,CAtegorySe
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CAtegorySe
    queryset = Category.objects.all()

class Xeberler(viewsets.ModelViewSet):
    serializer_class = NewSerializer
    queryset = REST.objects.all()


# def name(request):
#     a={
#         'xeberler':[]   
#         }
#     n = REST.objects.all()
#     for i in n:
#         a['xeberler'].append(
#          { 
#             'title': i.title,
#             'short': i.short_content,
#             'full':  i.full_content}
#         )
#     return JsonResponse(a)