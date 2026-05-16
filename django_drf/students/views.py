from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,filters
from .models import Students
from .serializers import StudentSerializer

#viewsets jis mai hamay automatically sara code mil jata hai put patch delte kai liye
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer

filter_backends=[DjangoFilterBackend,filters.SearchFilter]
filterset_fields=['course','marks']
search_fields=['name','email','course']
ordering_fields=['marks','created_at']

#Three methods there are pagination ,filtering ,searching ,pagination means kai 
# agr 1000 data sets hai tu wo aik baar nai diye ja skty with the sets of 10 students 
# record diye jaty hai taky server pr zyada load na ho aur filtering means
#  kai specific data chaye like jin students kai marks 80 hai unka data jin ki skill django 
# hai aur searching means kai hum jistrah browser pr likhty hai kai yr muje googgle ki website chaye ye search kro 
""" 
Api view jis mai hamay manuallyy sara code likhna prta hai dekte,post,put kai iye

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
class StudentDetailView(APIView):
    def get_object(self,pk):
      try:
         return Students.objects.get(pk=pk)
      except Students.DoesNotExist:
         return None
    def get(self,request,pk):
         student=self.get_object(pk)
         if not student:
           return Response(
                {'error': 'Student nahi mila'},
                status=status.HTTP_404_NOT_FOUND
            )
         serializer=StudentSerializer(student)
         return Response(serializer.data)
      
    def put(self,request,pk):
        student=self.get_object(pk)
        if not student:
           return Response(
               {'error': 'Student nahi mila'},
                status=status.HTTP_404_NOT_FOUND
           )
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
      student=self.get_object(pk)
      if not student:
        return Response(
            {'error': 'Student nahi mila'},   # ✅ error message
            status=status.HTTP_404_NOT_FOUND   # ✅ 404
        )
      student.delete()                           # ✅ ye line zaroori hai
      return Response(
        {'message': 'Student delete ho gaya!'},
        status=status.HTTP_204_NO_CONTENT
    ) """
      