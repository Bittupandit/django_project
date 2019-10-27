from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.product_name)