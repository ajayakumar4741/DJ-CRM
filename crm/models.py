from django.db import models

# Create your models here.

class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Records'
    
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')
    