from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length= 100)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    date_added_cart = models.DateField()

    def __str__(self):
        return f"{self.product_name}, {self.price}"
    
class Meta:
    db_table = "product"

    
            
            
            
           
