from django.db import models
from products.models import *

class Client(models.Model):
    c_name = models.CharField(max_length=100)
    c_phone = models.IntegerField(max_length=14)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def save_client(self):
        self.save()

    def delete_client(self):
        self.delete()

    def __str__(self):
        return f'{self.c_name}'

    class Meta:
        ordering = ['-date']