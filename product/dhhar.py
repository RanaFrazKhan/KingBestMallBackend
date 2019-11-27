import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KingBestMall.settings")
django.setup()
from product.models import *
from category.models import *
from django.db import connections
import requests
# from Course.models import *
# chapter=Chapters.objects.distinct( "course").exclude(isDeleted=True)
# curs=connections[ "dhaar"].cursor()
# curs.execute('select * from public."Products_main_categories"')
# curs.execute('select * from public."Products_sub_categories"')
# category=curs.fetchall()
# for i in category:
# #     # j=i[0]
#     curs.execute('select * from public."Products_main_categories" where id='+str(i[3])+'')
#     dhaar_cate=curs.fetchall()
#     print(dhaar_cate)
    # king_cat=Main_Categories.objects.get(Cat_Name=dhaar_cate[0][1])
    # sub=Sub_Categories.objects.create(Sub_Cat_Name=i[1],Subcat_Des=i[2],Cat_ID=king_cat)
    # print(sub)
#     main=Main_Categories.objects.create=(Cat_Name=i[1],Cat_Des=i[2],Pic=i[3])
#     sub=Sub_Categories.objects.create(Sub_Cat_Name=i[1],Subcat_Des=i[2],Cat_ID=main,Pic=i[4])
# print(category[0])
#
# category=curs.fetchall()
# for i in category:
#     print(i)

# curs.execute('select * from public."Products_phoneandtabletproduct"')
# raw_vedio = curs.fetchall()
# for i in raw_vedio:
#     # product=Product.objects.create(P_Title=i[2],P_Des=i[3],FixedPrice=i[14], Pic=i[17],count_no=i[27])#,Cat_Name=i[19],Sub_Cat_Name=i[20],Sub_Sub_Cat_Name=i[21],StoreName=i[23],
#     # print(i[16])
#     product=Product.objects.filter(P_Title=i[2]).update(Pic=i[16])
#     print(product)
# jewelry=Jewelry.objects.all()
# # product=Product.objects.filter()
# for i in jewelry:
#     price=Product.objects.get(id=i.Product_ID.id)
#     price.FixedPrice=price.FixedPrice+price.Discountprice
#     price.save()
product=Product.objects.filter(User_ID=9)
for i in product:
    print(i.Pic)
    # if (i.Pic=='201901101717092859.jpeg'):
    #     print("TRUE")
    #     new='https://storage.kingbestmall.com/images/'+i.Pic
    #     i.Pic=new
    #     i.save()