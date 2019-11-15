from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from attendanceManager.models import Teacher
from attendanceManager.models import Subjects
from attendanceManager.models import Students
from attendanceManager.models import Schedule
from attendanceManager.serializers import InitialStudentListSerializer
from attendanceManager.serializers import ScheduleModelSerializer
from attendanceManager.serializers import StudentsSerializer


def get_subject_slot(subjectid):
    subject = Subjects.objects.get(subjectiduq = subjectid)
    return subject.subjectslot

"""This is an auxillary function that returns students taking a particular subject and also returns 
necessary fields in the table"""
def get_students_by_subject(subject_id,subject_slot):
    fields = ["regdno", "name", "rollno"]
    if subject_slot == "subject1" :
        fields.append("subject1_at")
        return Students.objects.filter(subject1 = subject_id),fields
    elif subject_slot == "subject2" :
        fields.append("subject2_at")
        return Students.objects.filter(subject2 = subject_id),fields
    elif subject_slot == "subject3" :
        fields.append("subject3_at")
        return Students.objects.filter(subject3 = subject_id),fields
    elif subject_slot == "subject4" :
        fields.append("subject4_at")
        return Students.objects.filter(subject4 = subject_id),fields
    elif subject_slot == "subject5" :
        fields.append("subject5_at")
        return Students.objects.filter(subject5 = subject_id),fields
    elif subject_slot == "subject6" :
        fields.append("subject6_at")
        return Students.objects.filter(subject6 = subject_id),fields

def update_student_subject_attendance(student,subject_slot,student_data):
    if subject_slot == 'subject1' :
        student.update(subject1_at = student_data['subject1_at'])
    elif subject_slot == 'subject2' :
        student.update(subject2_at = student_data['subject2_at'])
    elif subject_slot == 'subject3' :
        student.update(subject3_at = student_data['subject3_at'])
    elif subject_slot == 'subject4' :
        student.update(subject4_at = student_data['subject4_at'])
    elif subject_slot == 'subject5' :
        student.update(subject5_at = student_data['subject5_at'])
    elif subject_slot == 'subject6' :
        student.update(subject6_at = student_data['subject6_at'])

"""This view retreives the initial list of students after the teacher has first logged in.
A nested dictionary object is returned which should be used to create and populate the tables in the Android App"""
@csrf_exempt
def get_initial_student_list(request,teacher_username):
    if request.method == 'GET':
        teacher = Teacher.objects.get(username = teacher_username)
        teacherId = teacher.pk
        #get the subjects the teacher teaches
        subjects = Subjects.objects.filter(subjectteacher = teacherId)
        students_per_subject = {}
        fields = []
        for subject in subjects:
            subject_id = subject.subjectid
            subject_slot = subject.subjectslot
            students, fields = get_students_by_subject(subject_id, subject_slot)
            students_serial = InitialStudentListSerializer(students,fields = fields,many = True)
            students_per_subject[subject.subjectiduq] = students_serial.data

        return JsonResponse(students_per_subject,status = status.HTTP_200_OK,safe=False)

@csrf_exempt
def get_teacher_routine(request,teacher_username):
    if request.method == 'GET':
        teacher = Teacher.objects.get(username = teacher_username)
        teacherId = teacher.pk
        week_routine = Schedule.objects.filter(teacherid = teacherId)
        teacher_routine = {}
        for day_routine in week_routine:
            time_schedule = ScheduleModelSerializer(day_routine)
            teacher_routine[day_routine.day] = time_schedule.data

        return(JsonResponse(teacher_routine,status = status.HTTP_200_OK,safe = False))


@csrf_exempt
def update_student_attendance(request):
    if request.method == 'PUT':
        parsed = JSONParser().parse(request)
        subjects = parsed.keys()
        for subject in subjects:
            students_per_subject = parsed[subject]
            for i in range(len(students_per_subject)):
                student_fresh_data = students_per_subject[i]
                student = Students.objects.filter(regdno = student_fresh_data['regdno'])
                subject_slot = get_subject_slot(subject)
                update_student_subject_attendance(student,subject_slot,student_fresh_data)

        return (JsonResponse({'msg':'successfull update'},status = status.HTTP_200_OK))


