from rest_framework import serializers
from attendanceManager.models import Teacher
from attendanceManager.models import Students
from attendanceManager.models import Schedule
from attendanceManager.models import Subjects


#To dynamically select fields during serialization
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields',None)

        super(DynamicFieldsModelSerializer,self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in (existing - allowed):
                self.fields.pop(field_name)


class TeacherSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=10,read_only=True)
    teacher_name = serializers.CharField(max_length=150)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=150)



class StudentsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150,read_only=True)
    rollno = serializers.IntegerField(read_only=True)
    semester = serializers.IntegerField(read_only=True)
    section = serializers.CharField(max_length=1,read_only=True)
    tgid = serializers.CharField(max_length=20,read_only=True)
    subject1 = serializers.CharField(max_length=20,read_only=True)
    subject2 = serializers.CharField(max_length=20,read_only=True)
    subject3 = serializers.CharField(max_length=20,read_only=True)
    subject4 = serializers.CharField(max_length=20,read_only=True)
    subject5 = serializers.CharField(max_length=20,read_only=True)
    subject6 = serializers.CharField(max_length=20,read_only=True)
    subject1_at = serializers.IntegerField()
    subject2_at = serializers.IntegerField()
    subject3_at = serializers.IntegerField()
    subject4_at = serializers.IntegerField()
    subject5_at = serializers.IntegerField()
    subject6_at = serializers.IntegerField()


class ScheduleSerializer(serializers.Serializer):
    pk = serializers.CharField(read_only=True,max_length=20)
    teacherid = serializers.CharField(read_only=True,max_length=20)
    day = serializers.CharField(read_only=True,max_length=10)
    from_9_10 = serializers.CharField(read_only=True,max_length=10)
    from_10_11 = serializers.CharField(read_only=True,max_length=10)
    from_11_12 = serializers.CharField(read_only=True,max_length=10)
    from_12_1 = serializers.CharField(read_only=True,max_length=10)
    from_2_3 = serializers.CharField(read_only=True,max_length=10)
    from_3_4 = serializers.CharField(read_only=True,max_length=10)
    from_4_5 = serializers.CharField(read_only=True,max_length=10)
    from_5_6 = serializers.CharField(read_only=True,max_length=10)


class SubjectsSerializer(serializers.Serializer):
    subjectiduq = serializers.CharField(read_only=True,max_length=20)
    subjectid = serializers.CharField(read_only=True,max_length=20)
    subjectTeacher = serializers.CharField(read_only=True,max_length = 20)
    totalclasses = serializers.IntegerField()
    semester = serializers.IntegerField(read_only=True)



class InitialStudentListSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Students
        fields = [
            'regdno',
            'name',
            'rollno',
            'subject1_at',
            'subject2_at',
            'subject3_at',
            'subject4_at',
            'subject5_at',
            'subject6_at'

        ]

class ScheduleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = [
            'from_9_10',
            'from_10_11',
            'from_11_12',
            'from_12_1',
            'from_2_3',
            'from_3_4',
            'from_4_5',
            'from_5_6',
        ]


