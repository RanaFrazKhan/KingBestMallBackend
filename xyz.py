import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KingBestMall.settings")
django.setup()
# dir_path = os.path.dirname(os.path.abspath(__file__))
import time
import pandas as pd
# import csv
import requests
print('mhsn')
df=pd.read_csv('/home/rana/Desktop/kingbestmallbackend/KingBestMall/category/FieldsName.csv')
print(df)
