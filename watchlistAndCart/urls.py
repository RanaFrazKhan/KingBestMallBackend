from django.urls import include,path
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'WatchList',Watchlist,basename='WatchList')
router.register(r'CartList',Cartlist,basename='CartList')
router.register(r'Coupons',Coupons,basename='Coupons')

urlpatterns=[
    path(r'',include(router.urls)),
]