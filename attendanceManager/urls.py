from django.conf.urls import url
from attendanceManager.views import get_initial_student_list
from attendanceManager.views import get_teacher_routine
from attendanceManager.views import update_student_attendance
from django.urls import path

app_name = 'attendanceManager'

urlpatterns = [
    path('initial_student_list/<str:teacher_username>',get_initial_student_list,name='fetch_initial_student_list'),
    path('get_teacher_routine/<str:teacher_username>',get_teacher_routine,name = 'fetch_teacher_routine'),
    path('update_student_attendance',update_student_attendance,name = "update_student_attendance")
]