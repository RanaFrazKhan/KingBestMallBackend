import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KingBestMall.settings")
django.setup()
dir_path = os.path.dirname(os.path.abspath(__file__))
import time
import pandas as pd
import csv
from category.models import *
import requests
import numpy
# print('mhsn')
df=pd.read_csv('/home/rana/Desktop/kingbestmallbackend/KingBestMall/category/FieldsName.csv')
new=df.to_numpy()
# print(new)
# for i in new:
# new=pd.DataFrame(new)
# input()
def mapping():
    repeat=[]
    # data_insertion()
    for data in new:
        print('data',data)
        li=[]
        sub_cat=Sub_Categories.objects.get(Sub_Cat_Name=data[0])
        print('sub',sub_cat)
        no_of_iterations=len(data)
        for i in range(1,no_of_iterations):
            if str(data[i])!='nan':
                print('ok')
                feature=Features.objects.get(Feature_Name=data[i])
                print('feature',feature.Feature_Name)
                li.append(feature.id)
            else:
                print('break')
                break
        # print('li',li)
        sub_cat.Feature.add(*li)
        print('repeat',repeat)
        # sub=sub_cat.save()
        # print('many',sub.id)

# mapping()

def check():
    feature=Features.objects.filter(Feature_Name='Type')
    for feature in feature:
        print(feature.Feature_Name)
        feature.delete()
        break
    print(Features.objects.filter(Feature_Name='Type').count())


# check()

# Features.objects.all().delete()
# print(Features.objects.all().count())
def subcatagories():
    sub_cat=Sub_Categories.objects.all()
    # for sub in sub_cat:
    # sub_cat.Feature.set=None
    # sub_cat.Feature.remove()
    # sub_cat.Feature.clear()
    sub_cat.Feature.through.objects.all().delete()
    sub_cat.save()
    # print(sub.id)
# subcatagories()
li=[]
def data_insertion():
    li = []
    for data in new:
        no_of_iterations = len(data)
        for i in range(1, no_of_iterations):
            if str(data[i]) != 'nan':
                li.append(data[i])
    new_list=set(li)
    print(new_list)
    print(len(new_list))
    for field in new_list:
        print(field)
        feature=Features.objects.create(Feature_Name=field)
        print(feature.id)

# data_insertion
def feature_data():
    li=[]
    feature=Features.objects.all()
    for feat in feature:
        li.append(feat.Feature_Name)
    dic={}
    dic.update({'name':li})
    df=pd.DataFrame(dic)
    print(df)

feature_data()
