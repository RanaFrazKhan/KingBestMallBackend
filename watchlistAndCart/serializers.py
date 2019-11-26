from  rest_framework import serializers
from .models import *
from product.serializers import ProductSerializer
class PostWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchProduct
        fields=('ProductID','User_ID')


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchProduct
        fields=('ProductID','User_ID','CreatedDate','inwatchlist')

class PostCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Checkout
        fields=('ProductID','User_ID','Quantity','promocode','incheckout')


class CheckoutSerializer(serializers.ModelSerializer):
    ProductID=ProductSerializer()
    class Meta:
        model=Checkout
        fields=('ProductID','User_ID','CreatedDate','Quantity','promocode','incheckout')

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiscountCoupons
        fields=( 'id','Discount','Day','StoreName','CouponsCode','ProductID','Quantity',)