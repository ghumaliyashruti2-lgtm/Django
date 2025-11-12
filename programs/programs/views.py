from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title' : 'homepage'
    }
    return render(request,"index.html",data)

def aboutus(request):
    return HttpResponse("welcome to shruti")

def courses(request):
    return HttpResponse("welcome to courses")

def course_details(request,course_id):
    return HttpResponse("welcome to " + str(course_id))
