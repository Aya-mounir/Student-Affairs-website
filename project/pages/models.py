from django.db import models


class Login(models.Model):
    username=models.CharField(max_length=25)
    password= models.CharField(max_length=25)
    

class Add(models.Model):
    x=[('male','male'),('female','female')]   
    y=[('Active','Active'),('Inactive','Inactive')]   
    z=[('CS','CS'),('IS','IS'),('AI','AI'),('IT','IT'),('DS','DS'),('General','General')]   
    
    Name=models.CharField(max_length=25)
    Id=models.CharField(max_length=10,primary_key=True)
    Gpa=models.DecimalField(max_digits=3,decimal_places=1)
    Email=models.EmailField(max_length=25)
    Mobile=models.CharField(max_length=12)
    Level=models.IntegerField()
    Date=models.CharField(blank=True,null=True,max_length=15)
    Gender=models.CharField(max_length=10,choices=x)
    Status=models.CharField(max_length=10,choices=y)
    Department=models.CharField(max_length=50,choices=z)
def __str__(self):
    return self.name