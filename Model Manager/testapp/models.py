from django.db import models
from django.db.models import Case, When, Value


class AgeCheckManager(models.Manager):
    def student_age(self):
        return self.annotate(
            classification=Case(
                When(age__gt=17, then=Value("Adult")),
                default=Value("Child")
                )
            )
    def active_filter(self):
        return self.filter(active=True)

class ActiveFilter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course, related_name="course")
    active = models.BooleanField(default=True)
    
    objects = models.Manager()
    studentfilter = ActiveFilter()

    def __str__(self):
        return self.firstname

    def age_check(self):
        if self.age:
            if self.age < 18:
                return "Child"
            else:
                return "Adult"
        else:
            return "no age defined"


