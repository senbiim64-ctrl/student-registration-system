# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    grade = models.IntegerField()
    date_of_birth = models.DateField()
    parent_contact = models.CharField(max_length=20,blank=True)
    address = models.TextField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
     
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
