from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
class StudentListView(APIView):
    def get(self,request):
        students=Students.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)


    def post(self,request):
     serializer=StudentSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)