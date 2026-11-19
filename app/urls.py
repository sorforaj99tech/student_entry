from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student_data, name= 'student_data_list'),
    path('about/', views.about),
    path('service/', views.service),
    path('teacher/', views.Teacher),
    path('result/',views.Result)
]
