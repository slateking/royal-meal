# # models.py

from django.db import models




class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default= 500.00)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=5.00)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)

    def __str__(self):
        return self.name
    
    def __str__(self):
        return '{} {}'.format(self.name, self.description)
    
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    


    


class Category(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='menu_images/category/')

    def __str__(self):
        return self.name