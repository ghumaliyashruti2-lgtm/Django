from django.http import HttpResponse,HttpResponseRedirect
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
    
def login(request):
    return render(request,"login.html")

def single(request):
    return render(request,"news-single.html")

def register(request):
    return render(request,"register.html")

def course(request):
    return render(request,"course-single.html")

def form(request):
    ans=0
    data = {}
    try :
        if request.method=="POST":
         #n1=int(request.GET['num1'])
         #n2=int(request.GET['num2'])
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         ans=n1+n2
         data = {
             'n1' : n1,
             'n2' : n2,
             'ans' : ans
         }
         
         return HttpResponseRedirect('/index/')
    except:
            pass     
    return render(request,"form.html",data)


