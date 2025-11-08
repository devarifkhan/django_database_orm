from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        # Create test data
        Student.objects.create(firstname='Alice', is_active=True)
        Student.objects.create(firstname='Bob', is_active=False)
        Student.objects.create(firstname='Charlie', is_active=True)

    def test_student_creation(self):
        """Test that students can be created"""
        alice = Student.objects.get(firstname='Alice')
        self.assertEqual(alice.firstname, 'Alice')
        self.assertTrue(alice.is_active)

    def test_custom_manager_methods(self):
        """Test custom manager methods"""
        active_students = Student.objects.get_active_students()
        self.assertEqual(active_students.count(), 2)

        a_students = Student.objects.get_students_by_name_starting_with('A')
        self.assertEqual(a_students.count(), 1)
        self.assertEqual(a_students.first().firstname, 'Alice')

    def test_queryset_operations(self):
        """Test various QuerySet operations"""
        # Test filtering
        inactive = Student.objects.filter(is_active=False)
        self.assertEqual(inactive.count(), 1)
        self.assertEqual(inactive.first().firstname, 'Bob')

        # Test ordering
        ordered = list(Student.objects.order_by('firstname').values_list('firstname', flat=True))
        self.assertEqual(ordered, ['Alice', 'Bob', 'Charlie'])

        # Test counting
        total = Student.objects.count()
        self.assertEqual(total, 3)
