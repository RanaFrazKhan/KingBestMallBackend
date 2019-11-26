from django.conf.urls import include
from django.urls import path,re_path

from rest_framework import routers
from .views import *
from rest_framework_nested import routers

router= routers.DefaultRouter()
router.register(r'List',List,basename='List')
# contact_router = routers.NestedSimpleRouter(router, r'List', lookup='List')
# contact_router.register(r'By', List, base_name='List-By')


urlpatterns = [
    re_path(r'(?:(?P<id>[0-9]+)/)?', include(router.urls)),
    path('Category/<int:pk>',MainCategory.as_view()),#get/ put / delete category
    path('SubCategory/<int:pk>',SubCategory.as_view()),#get/ put / delete subcategory
    path('NestedSubCategory/<int:pk>',NestedSubCategory.as_view()),#get/ put / delete subcategory
    # path('', include(contact_router.urls))
    # path('')

]
# urlpatterns=router.urls