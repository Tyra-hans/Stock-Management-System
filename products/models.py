from django.db import models

CATEGORY = (
    ('N','without chillie'),
    ('H',' hot chillie'),
    ('M','mild chillie'),
    ('SP','siri ya pilau'),
    ('SM','siri ya mchuzi'),
    ('SC','siri ya chai')
)

class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_image = models.ImageField(upload_to='images/')
    size = models.CharField(max_length=50)
    qyt = models.PositiveIntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=50,choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

    def __str__(self):
        return f'{self.p_name}'

    class Meta:
        ordering = ['-date']


