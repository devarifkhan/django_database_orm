import random
import factory
from django.contrib.auth.models import User
from factory.faker import faker

from .models import Student, Course

FAKE = faker.Faker()

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Sequence(lambda n: "Course_%d" % n)

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    firstname = factory.Faker('first_name')
    age = factory.Faker('random_number', digits=2)

    @factory.post_generation
    def course(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.course.add(*extracted)

