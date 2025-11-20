from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from service.models import Service
from courses.models import Courses
from .forms import py_Form
from news.models import News
from django.core.paginator import Paginator


#Homepage 
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


#newsdeatils
def newsdetails(request,new_slug):
    newsdetails=News.objects.get(new_slug= new_slug)
    data = {
        'newsdetails' : newsdetails 
    }
    return render(request,"newsdetails.html",data)


#about
def about(request):
    return render(request,"about.html")

#admissions
def admissions(request):
    return render(request,"admissions.html")

#contact
def contact(request):
    return render(request,"contact.html")

#def course-single(request):
    #return render(request,"course-single.html")
    
    
#courses
def courses(request):
    courses_data= Courses.objects.all() 
    paginator=Paginator(courses_data,1)
    page_number=request.GET.get('page')
    courses_datafinal = paginator.get_page(page_number)
    totalpage=courses_datafinal.paginator.num_pages
    #if request.method == "GET":
    #    ct = request.GET.get('search')
    #    if ct!=None:
    #        courses_data= Courses.objects.filter(courses_title__icontains=ct)
    data ={
        'courses_datas' : courses_datafinal,
        'lastpage': totalpage,
        'total_pages':[n+1 for n in range(totalpage)]
    }
    
    return render(request,"courses.html",data)    
    
    
#login    
def login(request):
    return render(request,"login.html")

#single
def single(request):
    return render(request,"news-single.html")


#register
def register(request):
    return render(request,"register.html")


#course
def course(request):
    return render(request,"course-single.html")


#calculator
#def calculator(request):
#    return render(request,"calculator.html")

#thankyou
def thankyou(request):
    if request.method == "POST":
        n1 = eval(request.POST.get('num1'))
        n2 = eval(request.POST.get('num2'))
        ans = n1 + n2
        return render(request, "thank-you.html", {'answer': ans})
    return render(request, "thank-you.html")


#form
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

#calculator
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

#evenodd
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
   
   
#marksheet
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