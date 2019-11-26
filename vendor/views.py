from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response

from core.serializer import *
from .models import *
from rest_framework import viewsets,mixins,generics, status
from rest_framework.decorators import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Vendor(viewsets.ViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    # queryset = StoreBankInformation.objects.all()
    # serializer_class = BankSerializer
    # permission_classes=[IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # @action(detail=False, )
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)
    #
    # def perform_create(self, serializer):
    #     serializer.save()

    @action(detail=False,methods=['post'])#post all store with bank information using nested serializer
    def Add(self,request):
        dic= request.data
        dic.update({'user1':request.user})
        serializer=VendorPostSerializer(data=dic)
        if serializer.is_valid():

            serializer.save()
        return Response(dic)

    @action(detail=False,methods=['get'])
    def GetStoreInformation(self,request):
        banks_info = []
        username = request.user.username
        print(username)
        user_id = User.objects.get(username=username)
        print('userid..', user_id.id)
        store_info = VendorStoreInformation.objects.filter(user1=user_id.id).filter(isdeleted=False).values()
        a = list(store_info)
        i = 0
        while i < store_info.count():
            print('IIII..', i)
            bank_info = StoreBankInformation.objects.filter(StoreID=a[i]['StoreName']).values()
            i += 1
            banks_info.append(bank_info)
        flattened = [val for sublist in banks_info for val in sublist]
        productList = [{'StoreInfo': store_info, 'BankInfo': flattened}]
        paginator = Paginator(productList, 10)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        items = paginator.count
        pages = paginator.num_pages
        res = {
            'Total Pages': pages,
            'Total Result': items,
            'Results': data.object_list,
        }
        return Response(res, status=status.HTTP_200_OK)

    @action(detail=False,methods=['delete'])#delete/Deactive stores
    def Delete(self,request,Vendor_pk):
        print('DELETE REQUEST')
        VendorStoreInformation.objects.filter(id=Vendor_pk).update(isdeleted=True)
        return Response({'msg': 'Store Deactivated Successfully...!!!'}, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])#Get all registered stores that are not deleted/deactivated
    def RegisteredStores(self,request):
        res = VendorStoreInformation.objects.filter(isdeleted=False).values('StoreName', 'userimage', 'banner')
        paginator = Paginator(res, 10)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        items = paginator.count
        pages = paginator.num_pages
        res = {
            'Total Pages': pages,
            'Total Result': items,
            'Results': data.object_list,
        }
        return Response(res, status=status.HTTP_200_OK)

class Subscribe(mixins.RetrieveModelMixin, #mixins for each user profile
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):#get profile
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update profile
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete profile
        return self.destroy(request, *args, **kwargs)