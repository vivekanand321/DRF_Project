from django.urls import path, include
from rest_framework import routers
from . import views
app_name="courses"
# router=routers.DefaultRouter()
# router.register('/',views.CourseListCreateView.as_view())
urlpatterns = [
    # path('', views.get_courses),
    # path('<int:pk>/', views.get_course),
    path('', views.CourseListCreateView.as_view(),name='courses'),

]