from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class VendorStoreInformation(models.Model):
    StoreName = models.CharField(max_length=250,unique=True,null=True,blank=True)
    OwnerName = models.CharField(max_length=255)
    BusinessEmail = models.EmailField(max_length=70, null=True, blank=True)
    Zip = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    OwnerContactNum = models.CharField(max_length=255,blank=True,null=True,default='NULL')
    BusinessPhone = models.CharField(max_length=255)
    Address= models.CharField(max_length=500)
    FbrRegister= models.BooleanField()
    LegalName= models.CharField(max_length=255, default='', blank=True)
    NTN= models.CharField(max_length=255, default= '', blank=True)
    STRN= models.CharField(max_length=255, default= '', blank=True)
    user1=models.ForeignKey(User, on_delete=models.CASCADE, default=None,blank=True,null=True)
    userimage = models.CharField(max_length=255, blank=True, null=True, default='NULL')
    banner = models.CharField(max_length=500, blank=True, null=True, default='NULL')
    activestore = models.BooleanField(default=True)
    isdeleted=models.BooleanField(default=False)

    def __str__(self):
        return str(self.StoreName)

class StoreBankInformation(models.Model):
    StoreID = models.ForeignKey(VendorStoreInformation, on_delete=models.CASCADE, to_field='StoreName', db_column='StoreName',related_name='StoreID')
    AccountTitle = models.CharField(max_length=255)
    AccountNumber = models.CharField(max_length=255)
    BankName = models.CharField(max_length=255)
    BranchName = models.CharField(max_length=255)
    BranchCode = models.CharField(max_length=255)

    def __str__(self):
        return str(self.AccountNumber)






