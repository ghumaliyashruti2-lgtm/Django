"""
URL configuration for programs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from programs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.homepage, name="index"),
    path('about/',views.about,name="about-us"),
    path('courses/',views.courses,name="courses"),
    path('contact/',views.contact,name="contact"),
    path('admissions/',views.admissions,name="admissions"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('single/',views.single,name="course-single-page"),
    path('course/',views.course,name="course-details"),
    path('form/',views.form,name="form"),
    path('thank-you/',views.thankyou,name="thankyou"),
    path('calculator/',views.calculator),
    path('evenodd/',views.evenodd),
    path('marksheet/',views.marksheet)
    ]
