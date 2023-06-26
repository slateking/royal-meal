from django.db import models

# Create your models here.

class Italian(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Italian_images/')
    price = models.DecimalField(max_digits=15, decimal_places=2, default= 500.00)
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=5.00)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)


    def __str__(self):
        return self.name
    
    def __str__(self):
        return '{} {}'.format(self.name, self.description)
    
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    