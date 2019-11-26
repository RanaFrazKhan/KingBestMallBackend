import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
from django.shortcuts import render
from django.utils.crypto import random
from rest_framework import mixins,viewsets,generics
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from watchlistAndCart.models import *
# from rest_framework.decorators import detail_route, list_route

# class Products(mixins.RetrieveModelMixin, #mixins for each product
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
#
#
#     def get(self, request, *args, **kwargs):  # get product
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):  # update product
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):  # delete product
#         return self.destroy(request, *args, **kwargs)
# @api_view(['POST'])
# def onePicUpload(request):
#     # try:
#         api_url = 'https://storage.kingbestmall.com/upload_image.php'
#         StoreName = request.data['StoreName']
#         print(StoreName)
#         ProductID = request.data['ProductID']
#         userdata0 = {'path': StoreName + '/' + ProductID + '/', 'filename': request.FILES['input_file'].name}
#         files0 = {'file': request.FILES['input_file'].read()}
#         a = requests.post(api_url, files=files0, params=userdata0,  verify=False)
#         print(a.reason)
#         print('ok')
#
#         return Response({'msg': a.content}, status=status.HTTP_200_OK)
    # except:
    #     return Response({'msg': 'Analysis Fail'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def page_offset(request):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1

    # print(page)
    items = page * 8
    offset = (page - 1) * 8
    print('items',items)
    print('pages',offset)
    return items,offset

class Product_CRUD(viewsets.ModelViewSet):#get/ put /post /delete product

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self,serializer_class):
        print(self.request.user.id)
        serializer_class.save(User_ID=self.request.user)



    def get_queryset(self,):
        print('id',self.request.user.id)
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(User_ID=self.request.user)
            print("query", queryset)
        return queryset
        # serializer_class(self.request.user)
        # return Response(status=status.HTTP_200_OK)
    # #
    # @action(detail=False , methods=['post'])
    # def post(self,serializer_class,):
    #     serializer_class.save(User_ID=self.request.user)
    #     product=request.data
    #     user=self.request.user
    #     dic=request.data
    #     dic.update({'User_ID':user})
    #     product=ProductSerializer(data=dic)
    #     if product.is_valid():
    #         product.save()
    #     return Response(serializer_class,status=status.HTTP_200_OK)

    # @detail_route(methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = ProductSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
class ProductListing(viewsets.ViewSet):#listing for products
    @action(detail=False, methods=['get'])
    def ByCategory(self,request,Products_pk):
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1

        print(page)
        items = page * 10
        offset = (page - 1) * 10
        print(offset)
        res = Product.objects.filter(Cat_Name=Products_pk)[offset:items]
        totalitems = int(Product.objects.filter(Cat_Name=Products_pk).count())
        totalpages = int(totalitems / 10)
        per = totalitems % 10
        if per != 0:
            totalpages += 1
        serializer = ProductSerializer(res, many=True)
        res = {
            'Total Result': totalitems,
            'Total Pages': totalpages,
            'Results': serializer.data
        }
        return Response({'Results': res}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def BySubCategory(self, request, Products_pk):
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1

        print(page)
        items = page * 10
        offset = (page - 1) * 10
        print(offset)
        res = Product.objects.filter(Sub_Cat_Name=Products_pk)[offset:items]
        totalitems = int(Product.objects.filter(Sub_Cat_Name=Products_pk).count())
        totalpages = int(totalitems / 10)
        per = totalitems % 10
        if per != 0:
            totalpages += 1
        serializer = ProductSerializer(res, many=True)
        res = {
            'Total Result': totalitems,
            'Total Pages': totalpages,
            'Results': serializer.data
        }
        return Response({'Results': res}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def ByNestedSubCategory(self, request, Products_pk):
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1

        print(page)
        items = page * 10
        offset = (page - 1) * 10
        print(offset)
        res = Product.objects.filter(Sub_Sub_Cat_Name=Products_pk)[offset:items]
        totalitems = int(Product.objects.filter(Sub_Sub_Cat_Name=Products_pk).count())
        totalpages = int(totalitems / 10)
        per = totalitems % 10
        if per != 0:
            totalpages += 1
        serializer = ProductSerializer(res, many=True)
        res = {
            'Total Result': totalitems,
            'Total Pages': totalpages,
            'Results': serializer.data
        }
        return Response({'Results': res}, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])
    def Recommended(self,request):
        productList = []
        if request.user.is_authenticated:
            items,offset=page_offset(request)
            get_all = Product.objects.all().exclude(User_ID=request.user).order_by('?')[offset:items]
            total_products = Product.objects.all().exclude(User_ID=request.user).count()
            totalpages = int(total_products / 8)

            per = total_products % 8
            if per != 0:
                totalpages += 1

            user = User.objects.get(username=request.user.username)
            GetWatch = WatchProduct.objects.filter(User_ID=user, ProductID__in=get_all)
            Getcheckout = Checkout.objects.filter(User_ID=user, ProductID__in=get_all)
            wishListCourses = [wish.ProductID for wish in GetWatch]
            checkListCourses = [check.product for check in Getcheckout]
            for course in get_all:
                serializer = ProductSerializer(course)
                courseData = serializer.data
                try:
                    if course in wishListCourses:
                        courseData.update({"inWishList": True})
                    else:
                        courseData.update({"inWishList": False})

                    if course in checkListCourses:
                        courseData.update({"inCheckoutList": True})
                    else:
                        courseData.update({"inCheckoutList": False})
                except:
                    pass
                productList.append({'product': courseData})
        else:
            get_all = Product.objects.all().order_by('?')[:12]
            for course in get_all:
                serializer = ProductSerializer(course)
                productList.append({'product': serializer.data})
        res = {
            'Results': productList,
        }
        return Response(res, status=status.HTTP_200_OK)


    @action(detail=False,methods=['get'])
    def FeatureDeals(self,request):
        productList = []
        if request.user.is_authenticated:
            get_all = Product.objects.all().order_by(
                '-count_no')[:12]
            user = User.objects.get(username=request.user.username)
            GetWatch = WatchProduct.objects.filter(User_ID=user, ProductID__in=get_all)
            Getcheckout = Checkout.objects.filter(User_ID=user, ProductID__in=get_all)
            wishListCourses = [wish.ProductID for wish in GetWatch]
            checkListCourses = [check.product for check in Getcheckout]
            for course in get_all:
                serializer = ProductSerializer(course)
                courseData = serializer.data
                try:
                    if course in wishListCourses:
                        courseData.update({"inWishList": True})
                    else:
                        courseData.update({"inWishList": False})

                    if course in checkListCourses:
                        courseData.update({"inCheckoutList": True})
                    else:
                        courseData.update({"inCheckoutList": False})
                except:
                    pass
                productList.append({'product': courseData})
        else:
            get_all = Product.objects.all().order_by('-count_no')[:12]
            for course in get_all:
                serializer = ProductSerializer(course)
                productList.append({'product': serializer.data})
        res = {
            'Results': productList,
        }
        return Response(res, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])
    def DailyDeals(self,request):
        productList = []
        if request.user.is_authenticated:
            get_all = Product.objects.all().order_by('-id')[:12]
            user = User.objects.get(username=request.user.username)
            GetWatch = WatchProduct.objects.filter(User_ID=user, ProductID__in=get_all)
            Getcheckout = Checkout.objects.filter(User_ID=user, ProductID__in=get_all)
            wishListCourses = [wish.ProductID for wish in GetWatch]
            checkListCourses = [check.ProductID for check in Getcheckout]
            for course in get_all:
                serializer = ProductSerializer(course)
                courseData = serializer.data
                try:
                    if course in wishListCourses:
                        courseData.update({"inWishList": True})
                    else:
                        courseData.update({"inWishList": False})

                    if course in checkListCourses:
                        courseData.update({"inCheckoutList": True})
                    else:
                        courseData.update({"inCheckoutList": False})
                except:
                    pass
                productList.append({'product': courseData})
        else:
            get_all = Product.objects.all().order_by('-id')[:12]
            for course in get_all:
                serializer = ProductSerializer(course)
                productList.append({'product': serializer.data})
        res = {
            'Results': productList,
        }
        return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def onePicUpload(request):
    # try:
    api_url = 'https://storage.kingbestmall.com/upload_image.php'
    print(request.FILES['input_file'])
    # StoreName = request.data['StoreName']
    # ProductID = request.data['ProductID']
    # userdata0 = {'path': StoreName + '/' + ProductID + '/', 'filename': request.FILES['input_file'].name}
    files0 = {'fileToUpload': request.FILES['input_file']}
    a = requests.post(api_url, files=files0,  verify=False)
    print(a.content)
    print('ok')

    return Response({'msg': a.content}, status=status.HTTP_200_OK)