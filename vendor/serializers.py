from rest_framework import serializers
from .models import *

class PostBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=StoreBankInformation
        fields=('id','AccountTitle','AccountNumber','BankName','BranchName','BranchCode')


class VendorPostSerializer(serializers.ModelSerializer):
    StoreID=PostBankSerializer(required=False)
    class Meta:
        model=VendorStoreInformation
        fields=('user1','StoreName','OwnerName','BusinessEmail','Zip','City','OwnerContactNum','BusinessPhone','Address','NTN','STRN','userimage','FbrRegister','LegalName','banner','StoreID')

    def create(self, validated_data):
        storeid = validated_data.pop('StoreID')
        bank = VendorStoreInformation.objects.create(**validated_data)
        store=StoreBankInformation.objects.create(StoreID=bank, **storeid)
        return bank

# class VendorUpdateSerializer(serializers.ModelSerializer):
#     StoreID=PostBankSerializer(required=False)
#     class Meta:
#     fields=('')

# class BankSerializer(serializers.ModelSerializer):
#     StoreID=VendorSerializer
#     class Meta:
#         model=StoreBankInformation
#         fields=['StoreID','AccountTitle','AccountNumber','BankName','BranchName','BranchCode']
#
#         def create(self, validated_data):
#             StoreID = validated_data.pop('StoreID')
#             musician = Books.objects.create(**validated_data)
#             Bid.objects.create(book=musician, **StoreID)
#             return musician