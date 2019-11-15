# Generated by Django 2.2.4 on 2019-10-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleid', models.CharField(db_column='scheduleId', max_length=45, primary_key=True, serialize=False)),
                ('teacherid', models.CharField(db_column='teacherId', max_length=45)),
                ('day', models.CharField(blank=True, max_length=45, null=True)),
                ('from_9_10', models.CharField(blank=True, db_column='9-10', max_length=45, null=True)),
                ('from_10_11', models.CharField(blank=True, db_column='10-11', max_length=45, null=True)),
                ('from_11_12', models.CharField(blank=True, db_column='11-12', max_length=45, null=True)),
                ('from_12_1', models.CharField(blank=True, db_column='12-1', max_length=45, null=True)),
                ('from_2_3', models.CharField(blank=True, db_column='2-3', max_length=45, null=True)),
                ('from_3_4', models.CharField(blank=True, db_column='3-4', max_length=45, null=True)),
                ('from_4_5', models.CharField(blank=True, db_column='4-5', max_length=45, null=True)),
                ('from_5_6', models.CharField(blank=True, db_column='5-6', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Schedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('regdno', models.IntegerField(db_column='regdNo', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('rollno', models.IntegerField(db_column='rollNo')),
                ('semester', models.IntegerField()),
                ('section', models.CharField(max_length=45)),
                ('tgid', models.CharField(db_column='tgId', max_length=45)),
                ('subject1', models.CharField(max_length=45)),
                ('subject2', models.CharField(max_length=45)),
                ('subject3', models.CharField(max_length=45)),
                ('subject4', models.CharField(max_length=45)),
                ('subject5', models.CharField(max_length=45)),
                ('subject6', models.CharField(max_length=45)),
                ('subject1_at', models.IntegerField(db_column='subject1_at')),
                ('subject2_at', models.IntegerField(db_column='subject2_at')),
                ('subject3_at', models.IntegerField(db_column='subject3_at')),
                ('subject4_at', models.IntegerField(db_column='subject4_at')),
                ('subject5_at', models.IntegerField(db_column='subject5_at')),
                ('subject6_at', models.IntegerField(db_column='subject6_at')),
            ],
            options={
                'db_table': 'Students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subjectiduq', models.CharField(db_column='subjectIdUq', max_length=45, primary_key=True, serialize=False)),
                ('subjectid', models.CharField(db_column='subjectId', max_length=45)),
                ('subjectteacher', models.CharField(db_column='subjectTeacher', max_length=45)),
                ('totalclasses', models.IntegerField(db_column='totalClasses')),
                ('semester', models.IntegerField()),
            ],
            options={
                'db_table': 'Subjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherid', models.CharField(db_column='teacherId', max_length=45, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Teacher',
                'managed': False,
            },
        ),
    ]