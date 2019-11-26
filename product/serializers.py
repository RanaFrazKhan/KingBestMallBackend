from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    # User_ID= serializers.(read_only=True)
    # User_ID = serializers.SerializerMethodField('_user',read_only=True)
    #
    # # Use this method for the custom field
    # def _user(self, obj):
    #     request = getattr(self.context, 'request', None)
    #     if request:
    #         return request.user.id
    class Meta:
        model=Product
        fields=('P_Title','User_ID','Cat_Name','StoreName','Sub_Cat_Name','Sub_Sub_Cat_Name','P_Des','P_Condition','Quantity','MaxQuantity',
                'Pic','DicountStatus','Discountprice','Discountpersentage','product_ad_active','FixedPrice','PurchasedPrice')

    # def create(self, validated_data):
    #     User_ID=self['user']
