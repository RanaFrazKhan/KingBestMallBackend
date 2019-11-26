from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from watchlistAndCart.models import Checkout
from product.models import *
from .models import *
from django.db.models import Avg,Sum
from .serializers import *
class Watchlist(viewsets.ViewSet):#watchlist apis for add
    permission_classes=[IsAuthenticated]
    @action(detail=False, methods=['post'])# add items to watchlist if it does not exist
    def Add(self,request):
        user=request.user
        dic = request.data
        dic.update({"User_ID": user})
        product_id = request.data['ProductID']
        if WatchProduct.objects.filter(Q(ProductID=product_id) & Q(User_ID=user)).exists():
            print('Product already')
            return Response({'Message': 'Product Already In Your WatchList'}, status=status.HTTP_201_CREATED)
        else:
            serializer=PostWatchlistSerializer(data=dic)
            if serializer.is_valid():
                serializer.save()
            return Response({'Message': 'Product Added Successfully In WatchList'}, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])#get all items from watchlist using pgination
    def Get(self,request):
        GetWatch = WatchProduct.objects.filter(User_ID=request.user)
        paginator = Paginator(GetWatch, 10)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = WatchlistSerializer(GetWatch, many=True)
        items = paginator.count
        pages = paginator.num_pages
        res = {
            'Total Result': items,
            'Total Pages': pages,
            'Results': serializer.data
        }

        return Response(res)

    @action(detail=False,methods=['delete'])#delete items from watchlist
    def Delete(self,request):
        product_id = request.data['ProductID']
        user=request.user
        if not WatchProduct.objects.filter(Q(User_ID=user)&Q(ProductID=product_id)).exists():
            print('NOT EXISTS..')
            return Response({'Message':'Product Not Exists Here..!!'},status=status.HTTP_200_OK)
        else:
            print('Exists..')
            WatchProduct.objects.filter(Q(User_ID=user) & Q(ProductID=product_id)).delete()
            return Response({'Message':'Product Deleted From Your Watchlist...!!'},status=status.HTTP_204_NO_CONTENT)

class Cartlist(viewsets.ViewSet):#Cartlist apis for add
    permission_classes=[IsAuthenticated]
    @action(detail=False, methods=['post'])#add item to cart if exists then sums the quantity
    def Add(self,request):
        user=request.user
        dic = request.data
        dic.update({"User_ID": user})
        product_id = request.data['ProductID']

        if Checkout.objects.filter(Q(ProductID=product_id) & Q(User_ID=user)).exists():
            existingcart=Checkout.objects.get(ProductID=product_id,User_ID=user)
            existingcart.Quantity=existingcart.Quantity+request.data['Quantity']
            existingcart.save()
            return Response({'Message': 'Product Added Successfully In Cart'}, status=status.HTTP_200_OK)

        else:
            serializer=PostCheckoutSerializer(data=dic)
            if serializer.is_valid():
                serializer.save()
            return Response({'Message': 'Product Added Successfully In Cart'}, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])#get all items from cart using pagination
    def Get(self,request):
        GetWatch = Checkout.objects.filter(User_ID=request.user)
        # avrg = Product.objects.all().aggregate(Avg('FixedPrice'))
        avrg = Checkout.objects.filter(User_ID=request.user).values('ProductID')
        # avrg2 = Checkout.objects.filter(User_ID=request.user).aggregate(Sum('Discountprice'))
        avrg1=Product.objects.filter(id__in=avrg).aggregate(Sum('FixedPrice'))
        avrg2=Product.objects.filter(id__in=avrg).aggregate(Sum('Discountprice'))
        print('average',avrg1,)
        print('average',avrg2)
        sum=round(avrg1['FixedPrice__sum'],2)
        dis=round(avrg2['Discountprice__sum'],2)
        difference=round(sum - dis,2)

        paginator = Paginator(GetWatch, 10)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CheckoutSerializer(GetWatch, many=True)
        items = paginator.count
        pages = paginator.num_pages
        res = {
            'Total Result': items,
            'Total Pages': pages,
            'Results': serializer.data,
            'Sum':sum,
            'Discount':dis,
            'difference':difference
        }

        return Response(res)

    @action(detail=False,methods=['delete'])#delete item from cart
    def Delete(self,request):
        product_id = request.data['ProductID']
        user=request.user
        if not Checkout.objects.filter(Q(User_ID=user)&Q(ProductID=product_id)).exists():
            print('NOT EXISTS..')
            return Response({'Message':'Product Not Exists Here..!!'},status=status.HTTP_200_OK)
        else:
            print('Exists..')
            Checkout.objects.filter(Q(User_ID=user) & Q(ProductID=product_id)).delete()
            return Response({'Message':'Product Deleted From Your Cart...!!'},status=status.HTTP_204_NO_CONTENT)

class Coupons(viewsets.ModelViewSet):
    queryset = DiscountCoupons.objects.all()
    serializer_class = CouponSerializer
