from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("welcome to shruti")

def courses(request):
    return HttpResponse("welcome to courses")

def course_details(request,course_id):
    return HttpResponse("welcome to " + str(course_id))
