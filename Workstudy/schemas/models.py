from django.db import models

# Create your models here.
#Admin Schema
class Admin(models.Model):
    admin_id= models.CharField(max_length=255,primary_key=True,choices=)
    admin_name = models.CharField(max_length=255)
    admin_email =models.EmailField()
    admin_phone =models.IntegerField(max_length=8)
#Job Schema
class Job(models.Model):
    job_id = models.CharField(max_length=255,primary_key=True)
    job_name = models.CharField(max_length=255)
    hourly_rate= models.IntegerField(max_length=16)
    admin_id= models.ForeignKey(Admin,on_delete=models.CASCADE)
#Student Schema
Gender =(
    ('M','M'),
    ('F','F')
)
class Student(models.Model):
    student_id= models.CharField(max_length=255,primary_key=True)
    student_name = models.CharField(max_length=255)
    student_email =models.EmailField()
    student_phone =models.IntegerField(max_length=8)
    level_of_study = models.IntegerField(max_length=1)
    gender = models.CharField(choices=Gender)

#Staff schema
class Staff(models.Model):
    staff_id= models.CharField(max_length=255,primary_key=True)
    staff_name = models.CharField(max_length=255)
    staff_email =models.EmailField()
    staff_phone =models.IntegerField(max_length=8)
    gender = models.CharField(choices=Gender)

#Application Schema
class Application(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    job_id =models.ForeignKey(Job,on_delete=models.CASCADE)
    application_status = models.BooleanField()

#Workdays Schema
class Workdays(models.Model):
    
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    job_id =models.ForeignKey(Job,on_delete=models.CASCADE)
    time_in= models.TimeField()
    time_out= models.TimeField()
    date= models.TimeField()
    record_id = models.CharField(max_length=255,unique=True)
    
