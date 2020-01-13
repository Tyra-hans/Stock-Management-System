from django.db import models

CATEGORY = (
    (categoryone,'categoryone'),
    (categoryone,'categoryone'),
    (categoryone,'categoryone'),
    (categoryone,'categoryone'),
    (categoryone,'categoryone'),
    (categoryone,'categoryone')
)

class Product(models.Model):
    p_name = models.CharField(max_lenght=100)
    p_image = models.ImageField(upload_to='images/')
    size = models.CharField(max_length=50)
    qyt = models.PositiveIntegerField()
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

    def __str__(self):
        return f'{self.p_name}'

    class Meta:
        ordering = ['-date']


