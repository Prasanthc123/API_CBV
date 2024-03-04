from django.db import models

# Create your models here.
class Productcategory(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_category=models.CharField(max_length=100)

    def __str__(self):
        return self.product_category

class Product(models.Model):
    Product_category_id=models.ForeignKey(Productcategory,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_cost=models.IntegerField()
    product_brand=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name