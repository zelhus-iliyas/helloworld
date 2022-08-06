from django.db import models


class Product(models.Model):  # Create your models here.

    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return "{}".format(self.title)
    
    
    
    
    @property
    def sale_price(self):
        return "%.2f" % (float(self.price)*0.2)
    