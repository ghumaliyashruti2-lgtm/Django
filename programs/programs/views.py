from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #data={
    #    'title' : 'homepage',
    #    'name' : ['riya','siya','priya'],
    #    'details' : [{'coursename' : 'html', 'fees' : 1200},
    #                 {'coursename' : 'python', 'fees' : 1500 }
    #                 ],
    #   'number' :[100,200,300,400,500]
    #    }
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def admissions(request):
    return render(request,"admissions.html")

def contact(request):
    return render(request,"contact.html")

#def course-single(request):
    #return render(request,"course-single.html")
    
def courses(request):
    return render(request,"courses.html")


