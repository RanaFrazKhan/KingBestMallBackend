from django.urls import include,path
from rest_framework import routers
from rest_framework_nested import routers
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,verify_jwt_token

router=routers.DefaultRouter()
router.register(r'users',UserViewSet)#get auth user info
# router.register(r'profile',UserProfile)#get user profile
# router.register(r'view', UserViewSet, basename='user')
router.register(r'ContactUs', ContactUs, basename='Contact_Us')#Contact us post and get all for admin
router.register(r'User', User_Profile, 'User')#User apis
router.register(r'Password', Password, 'Password')#User apis

contact_router = routers.NestedSimpleRouter(router, r'User', lookup='User')
contact_router.register(r'Verify', User_Profile, base_name='User-Username')


# router.register(r'mixins', SnippetDetail)#User apis
# router.register(r'Profile', Profile,)#User apis


urlpatterns=[
    path('', include(router.urls)),
    # path('Profile/<int:pk>/', Profile.as_view()),#url for get/put/delete user profile with mixins
    path('api-token-auth/', obtain_jwt_token),#login
    path('api-token-refresh/', refresh_jwt_token),#refresh token
    path('api-token-verify/', verify_jwt_token),# verify token
    path('', include(contact_router.urls)),
    path('check', check),


    # path('pass/', Set.as_view()),# verify token

#     url(r'^Contact-Us/$', views.contact_us, name='contact_us'),
# #####signup user my api ####
#     url(r'^signupuser/$', views.signup_user_),   #sign Up User
#
#     url(r'^UserFullDetailsPicUpload/(?P<pk>.+)$', views.UpdateUserCompleteDetailsPic),
#
#     # url(r'^GetallInvoiceIDByUser/(?P<pk>[0-9]+)$', views.GetInvoiceIDByUser),
#
#     url(r'^activate_account/$', views.active_account_),#Post api for activate the account
#Subscribe
#     url(r'^isActive/$', views.isActive), # Check activated account or not

]