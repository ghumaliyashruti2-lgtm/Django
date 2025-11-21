from django.contrib import admin
from courses.models import Courses
# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('courses_image','courses_title','courses_description')
admin.site.register(Courses,CoursesAdmin)

