from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('addstudent/', views.add_student, name='add_student'),
    path('updatestudent/', views.edit_student, name='edit_student'),
    path('deletestudent/', views.delete_student, name='delete_student'),
]