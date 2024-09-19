from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from django.core import serializers
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# @api_view(["GET"])
# def get_courses(request):
#     print("inside get_course api")
#     courses=Course.objects.all()
#     json_data=CourseSerializer(courses,many=True)
#     return Response(json_data.data)

# @api_view(["GET"])
# def get_course(request,pk):
#     print("**8******inside particular get_course api")
#     courses=Course.objects.filter(id=pk).first()
#     print("Course is ",courses)
#     json_data=CourseSerializer(courses)
#     return Response(json_data.data)

class CourseListCreateView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer