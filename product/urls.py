from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_nested import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'Product',Product_CRUD,basename='Product')#add delete update delete product using Modelviewset
router.register(r'Products',ProductListing,basename='Products')
nested=routers.NestedDefaultRouter(router,r'Products',lookup='Products')
nested.register(r'Listing',ProductListing,base_name='product-listing')


urlpatterns=[
    path('',include(router.urls)),
    # path('Product/<int:pk>',Products.as_view())
    path('',include(nested.urls)),
    path('picupload',onePicUpload),

]