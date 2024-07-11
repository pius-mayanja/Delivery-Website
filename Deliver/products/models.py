from django.db import models
from user.models import User



class Categories(models.Model):        
    category_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['category_name',]
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Categories, related_name='type',on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits = 30, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', null=True)
    is_available = models.BooleanField(default=True)
    product_by = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
   