from django.db import models
from product.models import *
from  vendor.models import *
# Create your models here.


class DiscountCoupons(models.Model):
    Discount = models.IntegerField()
    Day = models.IntegerField()
    Quantity = models.IntegerField()
    CouponsCode = models.CharField(max_length=255)
    ProductID = models.CharField(max_length=255, blank=True)
    StoreName =  models.ForeignKey(VendorStoreInformation, on_delete=models.CASCADE, to_field='StoreName',
                                  db_column='StoreName', default='Brainplow')
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.StoreName)

class WatchProduct(models.Model):
    ProductID = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    inwatchlist = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ProductID)

class Checkout(models.Model):
    ProductID = models.ForeignKey(Product,on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, default='',on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    promocode = models.ForeignKey(DiscountCoupons, null=True,on_delete=models.CASCADE,blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    incheckout = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ProductID)