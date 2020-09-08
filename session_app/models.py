from django.db import models


class instructor(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{name}'

class AddCourse(models.Model):
    course_title = models.CharField(max_length=100)
    course_category = models.CharField(max_length=150)
    instructor = models.ForeignKey(instructor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.course_title}'