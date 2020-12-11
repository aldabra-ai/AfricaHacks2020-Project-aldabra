from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from .models import StaticAppInfo
from .serializers import StaticinfoSerializer
from django.views.generic import TemplateView,CreateView





class IndexView(TemplateView):
    template_name = 'base/index.html'


# @api_view(['GET','POST'])
# def staticinfolist(request, format=None):

#     if request.method == 'GET':
#         static_info = StaticAppInfo.objects.all()
#         serializer = StaticinfoSerializer(static_info, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StaticinfoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def staticinfo_detail(request, pk, format=None):

#     try:
#         static_info = StaticAppInfo.objects.get(pk=pk)
#     except StaticAppInfo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = StaticinfoSerializer(StaticAppInfo)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StaticinfoSerializer(static_info, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'DELETE':
#         static_info.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

