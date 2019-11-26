from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_nested import routers

router=DefaultRouter()
router.register('Vendor',Vendor,basename='Vendor')#apis for vendor post with bank details
contact_router = routers.NestedSimpleRouter(router, r'Vendor', lookup='Vendor')
contact_router.register(r'Confirm', Vendor, base_name='Vendor-Information')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(contact_router.urls))

]