from django.db import models

class StudentManager(models.Manager):
    def get_students_by_name_starting_with(self, letter):
        return self.filter(firstname__startswith=letter)

    def get_active_students(self):
        # Assuming we add an is_active field later
        return self.filter(is_active=True)

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    # Custom manager
    objects = StudentManager()

    def __str__(self):
        return self.firstname
