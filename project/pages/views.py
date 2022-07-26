from ast import Delete
from email import message 
from tokenize import Name
from pages.admin import FciAdmin
from .models import Login
from django.db import models
from .models import Add 
from .models import *
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def allprojects(request):
    return render(request,'pages/allprojects.html')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=Login(username=username,password=password)
    return render(request,'pages/Login.html')

def home(request):
    return render(request,'pages/Home.html')

def add(request):
    
    if request.method=="POST":
        name = request.POST["name"]
        id = request.POST["id"]
        gpa = request.POST["gpa"]
        gender = request.POST["gender"]
        birth = request.POST["date"]
        level = request.POST["level"]
        system = request.POST["status"]
        prog = request.POST["department"]
        email = request.POST["Email"]
        mobile = request.POST["mob"]
        data=Add(Name=name,Id=id,Gpa=gpa,Email=email,Mobile=mobile,Level=level,Date=birth,Gender=gender,Status=system,Department=prog)
        
        if  0<=int(data.Gpa)<=4 and 1<=int(data.Level)<=4 and int(data.Id)>9999999 :
            data.save()
            messages.info(request,'add student successfully')
        else:
            messages.info(request,'add failed')
      
    return render(request,'pages/AddStudent.html')

def Edit(request,pk):
    return render(request,'pages/Edit.html',{'s':Add.objects.get(Id=pk)})

def Assignment(request,pk):
    return render(request,'pages/Assignment.html',{'s':Add.objects.get(Id=pk)})

def assignment(request):
    return render(request,'pages/Assignment.html')

def search(request):
    search = request.GET.get('search')
    if search:
        posts = Add.objects.filter(Q(Name=search) & Q(Name=search))
        return render(request,'pages/Search.html' , {'posts':posts})
 
    else:
        return render(request,'pages/Search.html' )

def viewstudent(request):
    students = Add.objects.all()
    return render(request,'pages/viewstudents.html',{"students":students}) 

def delete(request,pk):
    student=Add.objects.get(Id=pk)
    student.delete()
    return redirect('/edit')  

def editbutton(request,pk):
    std_pk=Add.objects.get(Id=pk)    
    if request.method=='POST':
        std_save=Add(request.POST,request.FILES,instance=std_pk)
        if std_save.is_valid():
            std_save.save()

            return redirect('/')
            
    else:
        std_save=Add(instance=std_pk)
        context={
            'student':std_save,

        } 
   
    return render(request,'pages/Edit.html',context)    

def edit(request):
        return render(request,'pages/Edit.html')    


def assignbutton(request,pk):
    std_pk=Add.objects.get(Id=pk)    
    if request.method=='POST':
        std_save=Add(request.POST,request.FILES,instance=std_pk)
        if std_save.is_valid():
            std_save.save()
            return redirect('/')
    else:
        std_save=Add(instance=std_pk)
        context={
            'student':std_save,
        }        
    return render(request,'pages/Assignment.html',context)   

def updaterecord(request, pk):
    
    name = request.POST['Name']
    gpa = request.POST["Gpa"]
    gender = request.POST["Gender"]
    birth = request.POST["date"]
    level = request.POST["Level"]
    system = request.POST["Status"]
    email = request.POST["email"]
    mobile = request.POST["Mob"]
    student = Add.objects.get(Id=pk)
    student.Name= name
    student.Gpa=gpa
    student.Gender=gender
    student.Date=birth
    student.Level=level
    student.Status=system
    student.Email=email
    student.Mobile=mobile
    student.save()
    return HttpResponseRedirect(reverse('edit'))


def assigndepart(request, pk):
    depart = request.POST['depart']
    student = Add.objects.get(Id=pk)
    if student.Level==3:
        student.Department=depart
        student.save()
    else:
        messages.info(request,'The student is not in Level 3')
    return HttpResponseRedirect(reverse('assignment'))

def active(request, pk):
    student = Add.objects.get(Id=pk)
    stat=student.Status
    if stat=='Active':
        stat='Inactive'
        student.Status=stat
    else:
        stat='Active'
        student.Status=stat
    student.save()
    return HttpResponseRedirect(reverse('view'))