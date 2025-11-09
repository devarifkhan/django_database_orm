# Queries Examples

## Specifying a Many-to-Many intermediate model
---
### Setup
```Python
import os
py manage.py shell
from ecommerce.inventory.models import Category
from ecommerce.inventory.models import Product
from ecommerce.inventory.models import Product_Category
os.system('cls')
```

### Query all
```
Product.objects.all()
Category.objects.all()
Product_Category.objects.all()
```
### Add new product
```
prod1 = Product(name="prod1", description="prod1", slug="prod1", is_active=True)
prod1.save()
prod2 = Product(name="prod2", description="prod2", slug="prod1", is_active=True)
prod2.save()
```
### Add new category
```
cat1 = Category(name="cat1", slug="cat1", is_active=True)
cat1.save()
cat2 = Category(name="cat2", slug="cat2", is_active=True)
cat2.save()
```
### Associate Product with Category
```
cat1 = Category.objects.get(name="cat1")
prod1 = Product.objects.get(name="prod1")
prod2 = Product.objects.get(name="prod2")
prod1.category.add(cat1)
prod2.category.add(cat1)
```
### Delete Link Table Instance
```
Product_Category.objects.get(id=1).delete()
```
### Delete Product/Category
```
Product.objects.get(id=1).delete()
```
### Associate Category with Product (Reverse m2m)
```
Category.objects.filter(id=1)
Category.objects.filter(product__id=1)
```
### All Products associated to X category
```
Product.objects.filter(category__id=3)
```
### Related Manager
```
prod = Product.objects.get(name="prod1")
prod.category.all()
cat = Category.objects.get(name="cat1")
cat.product.all() # Does not work
cat.product_set.all()

cat = Category.objects.get(name="cat1")
prod = Product.objects.get(name="prod2")
cat.product.add(prod)
```

### Additonal Fields
```
cat = Category.objects.get(name="cat2")
prod = Product.objects.get(name="prod2")
Product_Category.objects.create(product_id=prod, category_id=cat,order=1)  

cat2 = Category(name="cat2", slug="cat2", is_active=True).save()
prod.category.add(cat, through_defaults={'order': 1})
```