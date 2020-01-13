from django.db import models
from materials.models import *

class Supplier(models.Model):
    s_name = models.CharField(max_length=100)
    s_phone = models.CharField(max_length=14)
    date = models.DateTimeField(auto_now_add=True)
    materials = models.ForeignKey(Material, on_delete=models.CASCADE)

    def save_supplier(self):
        self.save()

    def delete_supplier(self):
        self.delete()

    def __str__(self):
        return f'{self.s_name}'

    class Meta:
        ordering = ['-date']

     
