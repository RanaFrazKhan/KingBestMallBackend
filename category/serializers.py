from rest_framework import serializers
from .models import *




class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Categories
        fields=('id','Cat_ID','Sub_Cat_Name','Subcat_Des','Pic')

class NestedSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Sub_Categories
        fields=('id','Sub_Cat_ID','Sub_Sub_Cat_Name','Sub_Subcat_Des','Pic')

class CategorySerializer(serializers.ModelSerializer):
    subcategory=SubCategorySerializer(many=True)
    class Meta:
        model = Main_Categories
        fields=('id','Cat_Name','Cat_Des','Pic','subcategory')