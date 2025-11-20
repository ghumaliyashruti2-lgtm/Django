from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from service.models import Service
from .forms import py_Form
from news.models import News

def homepage(request):
    services_data= Service.objects.all() # [:1] use for limit negative index not support 
    # services_data= Service.objects.order_by("id")  for accending
    # services_data= Service.objects.order_by("-id")  for desccending 
    news_data = News.objects.all()
    data = {
        'services_datas' : services_data,
        'news_data':news_data
    }
    return render(request,"index.html",data)


def newsdetails(request,id):
    newsdetails=News.objects.get(id= id)
    data = {
        'newsdetails' : newsdetails 
    }
    return render(request,"newsdetails.html",data)

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
        n1 = eval(request.POST.get('num1'))
        n2 = eval(request.POST.get('num2'))
        ans = n1 + n2
        return render(request, "thank-you.html", {'answer': ans})
    return render(request, "thank-you.html")



def form(request):
    ans=0
    varForm = py_Form()
    data = {'form':varForm}
    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
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
            n1 = eval(request.POST.get('val1'))
            n2 = eval(request.POST.get('val2'))
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


def evenodd(request):
    n1 = ""
    ans = ""
    if request.method == "POST":
        if request.POST.get('val1') == "":
             return render(request, "evenodd.html",{'error': True})
         
        n1 =eval(request.POST.get('val1'))
        if n1%2 == 0:
            ans = "Even"
        else:
            ans = "Odd"
    return render(request, "evenodd.html", {'ans': ans,'n1': n1})
    
def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('mark1'))
        s2 = eval(request.POST.get('mark2'))
        s3 = eval(request.POST.get('mark3'))
        s4 = eval(request.POST.get('mark4'))
        s5 = eval(request.POST.get('mark5'))
        totals = s1+s2+s3+s4+s5
        percentage = totals * 100 / 500
        if percentage >= 90:
            division = "first class"
        elif percentage >=80 and percentage <=90:
            division = "second class"
        elif percentage >=70 and percentage <=80:
            division = "third class"
        elif percentage >=35 and percentage <=70:
            division = "pass"
        else:
            division = "fail"   
        
        data = {
            'mark1' : s1,
            'mark2' : s2,
            'mark3' : s3,
            'mark4' : s4,
            'mark5' : s5,
            'total' : totals ,
            'per' : percentage,
            'div' : division
        }
        
        return render(request, "marksheet.html",data )
    return render(request, "marksheet.html")