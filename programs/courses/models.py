from django.db import models

class Courses(models.Model):
    courses_title=models.CharField(max_length=50)
    courses_description=models.TextField()
    courses_image =models.FileField(upload_to="courses/",max_length=250,null=True,default=None)
# Create your models here.
