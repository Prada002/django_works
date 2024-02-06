from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import datas, dept
import json

@permission_classes((AllowAny,))
class inputs(APIView):
    def get(self, request, name):
        print(name)
        data = datas.objects.all().values()
        return Response({'message': 'data retrieved', 'Status': 'Pass', 'data': data}, status=status.HTTP_200_OK)

    def post(self, request):
        data_add = datas.objects.create(
            NAME='rajan' ,
            EMAIL='pradapmail',
            PHONE='7598551381',
            department=1
        )
        print(request.data)
        return Response({'message': 'data retrieved', 'Status': 'Pass'}, status=status.HTTP_200_OK)

class department(APIView):
    def get(self, request):
        dept_data = dept.objects.all().values()
        return Response({'message': 'department data retrieved', 'Status': 'Pass', 'data': dept_data}, status=status.HTTP_200_OK)
    def post(self,request):
        dept_data=dept.objects.create(
            Depart="ECE"
            
        )
        return Response({'message': 'data retrieved', 'Status': 'Pass'}, status=status.HTTP_200_OK)


