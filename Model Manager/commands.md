from testapp.factory import StudentFactory

from testapp.factory import CourseFactory

StudentFactory.create_batch()

CourseFactory.create(name="science")

StudentFactory.create_batch(10, course="1")

from testapp.models import Course
