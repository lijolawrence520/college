from django.db import models

# Create your models here.
class Department(models.Model):
     name= models.CharField(max_length=250)

     def __str__(self):
         return self.name

class Course(models.Model) :
     department= models.ForeignKey(Department,on_delete=models.CASCADE)
     name=models.CharField(max_length=250)

     def __str__(self):
         return self.name

class Student(models.Model):

      name=models.CharField(max_length=250)
      department = models.ForeignKey(Department, on_delete=models.SET_NULL,blank=True,null=True)
      course= models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
      age=models.IntegerField()
      dob=models.DateField()
      address=models.TextField()
      email=models.EmailField()
      GENDER_CHOICES = (
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'),
      )

      gender = models.CharField(
          max_length=2,
          choices=GENDER_CHOICES,
          default='O',
      )

      PURPOSE_CHOICES = (
          ('M', 'Enquiry'),
          ('F', 'Place Order'),
          ('O', 'Return'),
          ('N', 'None')
      )

      purpose = models.CharField(
          max_length=2,
          choices=PURPOSE_CHOICES,
          default='N',
      )
      notebook=models.BooleanField(default=False)
      pen=models.BooleanField(default=False)
      exampaper=models.BooleanField(default=False)

      def __str__(self):
          return self.name