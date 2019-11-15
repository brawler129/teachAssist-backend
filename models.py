# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#This table contains schedule of every teacher.Each teacher has recurring rows i.e for each day of the week.
#scheduleid is derived like so scheduleid = teacherid + day
#from variables contain the subjectiduq
class Schedule(models.Model):
    scheduleid = models.CharField(db_column='scheduleId', primary_key=True, max_length=45)  # Field name made lowercase.
    teacherid = models.CharField(db_column='teacherId', max_length=45)  # Field name made lowercase.
    day = models.CharField(max_length=45, blank=True, null=True)
    from_9_10 = models.CharField(db_column='9-10', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_10_11 = models.CharField(db_column='10-11', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_11_12 = models.CharField(db_column='11-12', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_12_1 = models.CharField(db_column='12-1', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_2_3 = models.CharField(db_column='2-3', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_3_4 = models.CharField(db_column='3-4', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_4_5 = models.CharField(db_column='4-5', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    from_5_6 = models.CharField(db_column='5-6', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Schedule'


class Students(models.Model):
    regdno = models.IntegerField(db_column='regdNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    rollno = models.IntegerField(db_column='rollNo')  # Field name made lowercase.
    semester = models.IntegerField()
    section = models.CharField(max_length=45)
    #Teacher Guardian ID
    tgid = models.CharField(db_column='tgId', max_length=45)  # Field name made lowercase.
    #Subject IDs
    subject1 = models.CharField(max_length=45)
    subject2 = models.CharField(max_length=45)
    subject3 = models.CharField(max_length=45)
    subject4 = models.CharField(max_length=45)
    subject5 = models.CharField(max_length=45)
    subject6 = models.CharField(max_length=45)
    #Subject Attendance i.e the number of classes attended in that subject
    subject1_at = models.IntegerField(db_column='subject1_at')  # Field renamed to remove unsuitable characters.
    subject2_at = models.IntegerField(db_column='subject2_at')  # Field renamed to remove unsuitable characters.
    subject3_at = models.IntegerField(db_column='subject3_at')  # Field renamed to remove unsuitable characters.
    subject4_at = models.IntegerField(db_column='subject4_at')  # Field renamed to remove unsuitable characters.
    subject5_at = models.IntegerField(db_column='subject5_at')  # Field renamed to remove unsuitable characters.
    subject6_at = models.IntegerField(db_column='subject6_at')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Students'


class Subjects(models.Model):
    subjectiduq = models.CharField(db_column='subjectIdUq', primary_key=True, max_length=45)  #subjectid + Section
    subjectid = models.CharField(db_column='subjectId', max_length=45)
    subjectteacher = models.CharField(db_column='subjectTeacher', max_length=45)  # Subject teacher id
    totalclasses = models.IntegerField(db_column='totalClasses')  # count of how many classes have been taken
    subject_slot = models.CharField(db_column="subject_slot",max_length=20)
    semester = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Subjects'


class Teacher(models.Model):
    teacherid = models.CharField(db_column='teacherId', primary_key=True, max_length=45)  # Field name made lowercase.
    teacher_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Teacher'
