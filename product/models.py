from django.db import models
from django.contrib.auth.models import User
from core.models import *
from category.models import *
from vendor.models import *
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField


# Create your models here.

class Product(models.Model):#model for generic features for a product
    P_Title = models.CharField(max_length=255, null=True, blank=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default='')
    StoreName = models.ForeignKey(VendorStoreInformation, on_delete=models.CASCADE, to_field='StoreName',
                                  db_column='StoreName', null=True, blank=True)
    Cat_Name = models.ForeignKey(Main_Categories, on_delete=models.CASCADE, db_index=True, to_field='Cat_Name',
                                 db_column='Cat_Name', null=True, blank=True)
    Sub_Cat_Name = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE, to_field='Sub_Cat_Name',
                                     db_column='Sub_Cat_Name', null=True, blank=True)
    Sub_Sub_Cat_Name = models.ForeignKey(Sub_Sub_Categories, on_delete=models.CASCADE, to_field='Sub_Sub_Cat_Name',
                                         db_column='Sub_Sub_Cat_Name', null=True, blank=True)
    P_Des = models.CharField(max_length=15000, null=True, blank=True)
    P_Condition = models.CharField(max_length=255, null=True, blank=True)
    Active = models.BooleanField(default=False)
    Sold = models.BooleanField(default=False)
    Quantity = models.IntegerField(null=True, blank=True)
    MaxQuantity = models.IntegerField(default=0, null=True, blank=True)
    Pic = models.TextField(default='', blank=True, null=True)
    DicountStatus = models.BooleanField(default=False)
    Discountprice = models.FloatField(null=True, blank=True)
    Discountpersentage = models.FloatField(null=True, blank=True)
    product_ad_active = models.BooleanField(default=False)
    aproval = models.BooleanField(default=False)
    count_no = models.IntegerField(default=0, null=True, blank=True)
    FixedPrice = models.FloatField(max_length=256, null=True, blank=True,default=0)
    PurchasedPrice=models.FloatField(null=True,blank=True,default=0)


    def __str__(self):
        return str(self.P_Title)

class Feature_Value(models.Model):#
    Sub_Categories_Id = models.ForeignKey(Sub_Categories,null=True,blank=True,on_delete=models.CASCADE)
    Feature_Id = models.ForeignKey(Features,null=True,blank=True,on_delete=models.CASCADE)
    Feature_Value = models.CharField(max_length=200,null=True,blank=True)
    General_Features=models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.Feature_Value

class Jewelry(models.Model):#model for johnnyscustomjewelry
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, default='')
    Brand=models.CharField(max_length=20000,null=True,blank=True)
    SKU=models.CharField(max_length=20000,null=True,blank=True)#stock keeping unit
    MetalType=models.CharField(max_length=20000,null=True,blank=True)#
    MetalColor=models.CharField(max_length=20000,null=True,blank=True)#
    MoldKit=models.CharField(max_length=20000,null=True,blank=True)#
    TopBottom=models.CharField(max_length=20000,null=True,blank=True)#
    PC=models.CharField(max_length=20000,null=True,blank=True)#
    Size=models.CharField(max_length=20000, null=True, blank=True)
    ChainType=models.CharField(max_length=20000,null=True, blank=True)
    Color=models.CharField(max_length=20000,null=True, blank=True)
    Letter=models.CharField(max_length=20000,null=True, blank=True)
    StoreName=models.CharField(max_length=20000,null=True, blank=True)


class ProductsReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='',null=True,blank=True)
    Product_Id = models.CharField(max_length=256,default='NULL',blank=True,null=True)
    Reviews = models.CharField(max_length=10000000)
    Rating = models.DecimalField(max_digits=5, decimal_places=1)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user.username)


class Recently_Items(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, default='',on_delete=models.CASCADE)
    user = models.ForeignKey(User, default='', null=True, blank=True,on_delete=models.CASCADE)
    Cat_Name = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.product.ProductID