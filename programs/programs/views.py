from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("welcome to shruti")

def courses(request):
    return HttpResponse("welcome to courses")

