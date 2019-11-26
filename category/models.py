from django.db import models
# from product.models import Features
# Create your models here.
class Main_Categories(models.Model):
    Cat_Name = models.CharField(max_length=255, unique=True)
    Cat_Des = models.CharField(max_length=255,null=True,blank=True)
    Pic = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.Cat_Name)

class Features(models.Model):
    Feature_Name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Feature_Name

class Sub_Categories(models.Model):
    Cat_ID=models.ForeignKey(Main_Categories,on_delete=models.CASCADE,related_name='subcategory')
    Sub_Cat_Name = models.CharField(max_length=255, unique=True)
    Subcat_Des = models.CharField(max_length=255,null=True,blank=True)
    Pic = models.CharField(max_length=255, default='',null=True,blank=True)
    Feature = models.ManyToManyField(Features,null=True, blank=True)

    def __str__(self):
        return str(self.Sub_Cat_Name)

class Sub_Sub_Categories(models.Model):
    Sub_Cat_ID=models.ForeignKey(Sub_Categories,on_delete=models.CASCADE)
    # Cat_ID = models.ForeignKey(Main_Categories,on_delete=models.CASCADE)
    Sub_Sub_Cat_Name = models.CharField(max_length=255, unique=True)
    Sub_Subcat_Des = models.CharField(max_length=255,null=True,blank=True)
    Pic = models.CharField(max_length=255, default='',null=True,blank=True)



    def __str__(self):
        return str(self.Sub_Sub_Cat_Name)

# class Feature_Value(models.Model):
#     Sub_Categories_Id = models.ForeignKey(Sub_Categories,null=True,blank=True,on_delete=models.CASCADE)
#     Feature_Id = models.ForeignKey(Features,null=True,blank=True,on_delete=models.CASCADE)
#     Feature_Value = models.CharField(max_length=200,null=True,blank=True)
#
#     def __str__(self):
#         return self.Feature_Value