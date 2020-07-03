from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class SciFi(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, 
        blank=True, related_name='Children')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name