from django.db import models

class ProductIDField(models.CharField):

    description = "A unique product identifier"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)

from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):

    description = "An integer field for object ordering"

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                obj = self.model.objects.latest(self.attname)
                value = obj.order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        else:
            return super().pre_save(model_instance, add)
        
        
class HexColorField(models.CharField):
    
    description = "A string field for hexadecimal color values"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        super().__init__(*args, **kwargs)
    
    def db_type(self, connection):
        return 'INTEGER(3)'

    def get_prep_value(self, value):
        if value is None:
            return None
        return int(value, 16)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        hex_value = format(value, 'X')
        return hex_value