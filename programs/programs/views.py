from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import py_Form

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

def calculator(request):
    return render(request,"calculator.html")


def thankyou(request):
    if request.method == "POST":
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        ans = n1 + n2
        return render(request, "thank-you.html", {'answer': ans})
    return render(request, "thank-you.html")



def form(request):
    ans=0
    varForm = py_Form()
    data = {'form':varForm}
    if request.method=="POST":
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        ans=n1+n2
        data = {
            'n1' : n1,
            'n2' : n2,
            'answer' : ans,
            'form':varForm       
        }
        return HttpResponseRedirect("/thank-you/",data)
    return render(request,"form.html",data)


def calculator(request):
    ans = ""
    n1 = ""
    n2 = ""
    opr = ""

    try:
        if request.method == "POST":
            n1 = int(request.POST.get('val1'))
            n2 = int(request.POST.get('val2'))
            opr = request.POST.get('opr')

            match opr:
                case '+':
                    ans = n1 + n2
                case '-':
                    ans = n1 - n2
                case '*':
                    ans = n1 * n2
                case '/':
                    ans = n1 / n2
                case _:
                    ans = "Invalid operator"

    except Exception as e:
        ans = "Invalid operator .."

    return render(request, "calculator.html", {
        'ans': ans,
        'n1': n1,
        'n2': n2,
        'opr': opr
    })

    

