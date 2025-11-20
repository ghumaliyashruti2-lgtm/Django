from django.db import models

class Courses(models.Model):
    courses_title=models.CharField(max_length=50)
    courses_description=models.TextField()
# Create your models here.
