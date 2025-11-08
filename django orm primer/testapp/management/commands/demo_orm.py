from django.core.management.base import BaseCommand
from testapp.models import Student

class Command(BaseCommand):
    help = 'Demonstrates Django ORM Model Manager and QuerySet usage'

    def handle(self, *args, **options):
        self.stdout.write('=== Django ORM Primer Demo ===\n')

        # Clear existing data
        Student.objects.all().delete()

        # Create sample data
        self.stdout.write('Creating sample students...')
        Student.objects.create(firstname='Alice', is_active=True)
        Student.objects.create(firstname='Bob', is_active=False)
        Student.objects.create(firstname='Charlie', is_active=True)
        Student.objects.create(firstname='David', is_active=True)
        Student.objects.create(firstname='Eve', is_active=False)
        self.stdout.write('Done!\n')

        # Demonstrate Model Manager methods
        self.stdout.write('=== Model Manager Methods ===')
        active_students = Student.objects.get_active_students()
        self.stdout.write(f'Active students: {[s.firstname for s in active_students]}')

        a_students = Student.objects.get_students_by_name_starting_with('A')
        self.stdout.write(f'Students starting with A: {[s.firstname for s in a_students]}\n')

        # Demonstrate QuerySet operations
        self.stdout.write('=== QuerySet Operations ===')

        # All students
        all_students = Student.objects.all()
        self.stdout.write(f'All students: {[s.firstname for s in all_students]}')

        # Filtering
        inactive_students = Student.objects.filter(is_active=False)
        self.stdout.write(f'Inactive students: {[s.firstname for s in inactive_students]}')

        # Using exclude
        active_students_qs = Student.objects.exclude(is_active=False)
        self.stdout.write(f'Active students (using exclude): {[s.firstname for s in active_students_qs]}')

        # Field lookups
        c_students = Student.objects.filter(firstname__startswith='C')
        self.stdout.write(f'Students starting with C: {[s.firstname for s in c_students]}')

        # Ordering
        ordered_students = Student.objects.order_by('firstname')
        self.stdout.write(f'Students ordered by name: {[s.firstname for s in ordered_students]}')

        # Limiting
        first_two = Student.objects.all()[:2]
        self.stdout.write(f'First 2 students: {[s.firstname for s in first_two]}')

        # Counting
        total_count = Student.objects.count()
        active_count = Student.objects.filter(is_active=True).count()
        self.stdout.write(f'Total students: {total_count}, Active: {active_count}')

        # Aggregation
        from django.db.models import Count, Q
        stats = Student.objects.aggregate(
            total=Count('id'),
            active_count=Count('id', filter=Q(is_active=True))
        )
        self.stdout.write(f'Aggregation stats: Total={stats["total"]}, Active={stats["active_count"]}')

        self.stdout.write('\n=== Demo Complete ===')