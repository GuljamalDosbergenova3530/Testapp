from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True )
    
    
    def __str__(self):
        return self.name
    
class Meta:
        ordering = [ '-id' ]

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=True, null=False)
    image= models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name