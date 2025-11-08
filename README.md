# Django Database ORM Primer

This project demonstrates the fundamentals of Django's Object-Relational Mapping (ORM) system, focusing on Model Managers and QuerySets.

## Model Manager Primer

Model Managers in Django provide the interface for database query operations. Every Django model has at least one manager, and you can define custom managers to encapsulate common query logic.

### Default Manager
By default, Django provides a `Manager` instance called `objects` for every model:

```python
students = Student.objects.all()  # Returns all Student instances
```

### Custom Managers
You can create custom managers by subclassing `models.Manager` and overriding methods or adding new ones:

```python
class StudentManager(models.Manager):
    def get_students_by_name_starting_with(self, letter):
        return self.filter(firstname__startswith=letter)

    def get_active_students(self):
        return self.filter(is_active=True)

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = StudentManager()  # Custom manager
```

### Using Custom Managers
```python
# Get all students whose name starts with 'A'
a_students = Student.objects.get_students_by_name_starting_with('A')

# Get only active students
active_students = Student.objects.get_active_students()
```

## QuerySet Primer

A QuerySet represents a collection of database objects. QuerySets are lazy - they don't hit the database until you evaluate them.

### Creating QuerySets

```python
# All students
all_students = Student.objects.all()

# Filtered students
active_students = Student.objects.filter(is_active=True)
inactive_students = Student.objects.exclude(is_active=True)

# Single object (raises exception if not found)
student = Student.objects.get(id=1)

# Single object (returns None if not found)
student = Student.objects.filter(id=1).first()
```

### Chaining Filters

QuerySets are chainable:

```python
# Chain multiple filters
students = Student.objects.filter(is_active=True).filter(firstname__startswith='J')
```

### Field Lookups

Django provides various field lookups for filtering:

```python
# Exact match
Student.objects.filter(firstname='John')

# Case-insensitive match
Student.objects.filter(firstname__iexact='john')

# Starts with
Student.objects.filter(firstname__startswith='Jo')

# Contains
Student.objects.filter(firstname__contains='oh')

# In a list
Student.objects.filter(id__in=[1, 2, 3])

# Greater than
Student.objects.filter(id__gt=5)

# Less than or equal
Student.objects.filter(id__lte=10)
```

### Ordering

```python
# Order by firstname ascending
Student.objects.order_by('firstname')

# Order by firstname descending
Student.objects.order_by('-firstname')

# Multiple fields
Student.objects.order_by('is_active', '-firstname')
```

### Limiting Results

```python
# First 5 students
Student.objects.all()[:5]

# Students 6-10
Student.objects.all()[5:10]
```

### Aggregation

```python
from django.db.models import Count, Avg, Max, Min

# Count students
total_students = Student.objects.count()

# Count active students
active_count = Student.objects.filter(is_active=True).count()

# Get statistics
stats = Student.objects.aggregate(
    total=Count('id'),
    active_count=Count('id', filter=models.Q(is_active=True))
)
```

### Updating Objects

```python
# Update all students to inactive
Student.objects.update(is_active=False)

# Update specific students
Student.objects.filter(firstname__startswith='J').update(is_active=True)
```

### Deleting Objects

```python
# Delete all inactive students
Student.objects.filter(is_active=False).delete()

# Delete specific student
student = Student.objects.get(id=1)
student.delete()
```

## Running the Project

1. Install Django:
   ```bash
   pip install django
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing the ORM

You can test these concepts in Django's shell:

```bash
python manage.py shell
```

Then in the shell:
```python
from testapp.models import Student

# Create some students
Student.objects.create(firstname='Alice', is_active=True)
Student.objects.create(firstname='Bob', is_active=False)
Student.objects.create(firstname='Charlie', is_active=True)

# Test custom manager methods
active_students = Student.objects.get_active_students()
a_students = Student.objects.get_students_by_name_starting_with('A')

# Test QuerySet operations
all_students = Student.objects.all()
inactive_students = Student.objects.filter(is_active=False)
```

### Running the Demo

A management command is provided to demonstrate all concepts:

```bash
python manage.py demo_orm
```

This command will:
- Create sample student data
- Demonstrate custom manager methods
- Show various QuerySet operations (filtering, ordering, limiting, aggregation)

### Running Tests

Run the unit tests to verify the ORM functionality:

```bash
python manage.py test
```

The tests cover:
- Model creation and basic operations
- Custom manager methods
- QuerySet filtering, ordering, and counting operations