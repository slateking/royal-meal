from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
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


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default= 500.00)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
