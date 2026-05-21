""" from django.urls import path
from.views import StudentListView,StudentDetailView
urlpatterns = [
    path('students/',StudentListView.as_view(),name='student-list'),
    path('students/<int:pk>/',StudentDetailView.as_view(),name='student-detail')
]
 """
from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet,RegisterView
router=routers.DefaultRouter()
router.register('students',StudentViewSet,basename='student')
urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
]
