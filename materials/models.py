from django.db import models

class Material(models.Model):
    m_name = models.CharField(max_length=100)
    qyt = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def save_material(self):
        self.save()

    def delete_material(self):
        self.delete()

    def __str__(self):
        return f'{self.m_name}'

    class Meta:
        ordering = ['date']
