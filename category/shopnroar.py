import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KingBestMall.settings")
django.setup()
from category.models import *
from django.db import connections
import requests

# data=requests.get('https://backend.shopnroar.com/products/GetAllCategories').json()
# target=data['Categories']
# for i in target:
#         main=Main_Categories.objects.create(Cat_Name=i['Category'],Pic=i['path'],Cat_Des='ShopnRoarCategory')
#         print('cate     ',main.id)
#         sub=i['SubCategories']
#         for j in sub:
#             print(j)
#             subdata=Sub_Categories.objects.create(Sub_Cat_Name=j['SubCat'],Subcat_Des='ShopnRoarSubCategory',Cat_ID=main)
#             print('sub      ',subdata.Cat_ID)#     # print(i)

# import pandas
# df = pandas.read_csv('FieldsName.csv', error_bad_lines=False)
# # sub=Sub_Categories.objects.all()
# # for i in sub:
# #     print(i.Sub_Cat_Name)
# # df.head()
# # print(df)
# for j in df:
#     # print(j)
#     for k in j:
#         print(k)

import csv

# print("here")
# MixList = []
oldfile = open('/home/rana/Desktop/kingbestmallbackend/KingBestMall/category/FieldsName.csv')
read = csv.reader(oldfile)
# print(read)
count=0
for data in read:
    # print(data)
    sub=Sub_Categories.objects.get(Sub_Cat_Name=data[0])
    print('name         ',sub.Sub_Cat_Name)
    for j in data:
        if j!='' and j!=sub.Sub_Cat_Name:
            # count=count+1
            # feature=Features.objects.create(Feature_Name=j)
            print(j)

    print('//////////////')