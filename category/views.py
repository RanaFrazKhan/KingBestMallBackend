from django.shortcuts import render
from rest_framework import viewsets,mixins,generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .models import *
from .serializers import *
# Create your views here.
class MainCategory(mixins.RetrieveModelMixin, #mixins for each Category
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Main_Categories.objects.all()
    serializer_class = CategorySerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):#get Category
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update Category
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete Category
        return self.destroy(request, *args, **kwargs)

class SubCategory(mixins.RetrieveModelMixin, #mixins for each subCategory
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Sub_Categories.objects.all()
    serializer_class = SubCategorySerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):#get subCategory
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update subCategory
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete subCategory
        return self.destroy(request, *args, **kwargs)

class NestedSubCategory(mixins.RetrieveModelMixin, #mixins for each subCategory
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Sub_Sub_Categories.objects.all()
    serializer_class = NestedSubCategorySerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):#get subCategory
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update subCategory
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete subCategory
        return self.destroy(request, *args, **kwargs)

class List(viewsets.ViewSet):
    @action(detail=False,methods=['get'])
    def Category(self,request,id):

        category=Main_Categories.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def SubCategory(self, request,id):
        if id:
            subcategory = Sub_Categories.objects.filter(Q(Cat_ID=id)|Q(Sub_Cat_Name=id)).order_by('id')
            serializer = SubCategorySerializer(subcategory, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            subcategory = Sub_Categories.objects.all().order_by('id')
            serializer = SubCategorySerializer(subcategory,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])
    def NestedSubCategory(self,request,id):
        if id:
            nested = Sub_Sub_Categories.objects.filter(Q(Sub_Cat_ID=id)|Q(Sub_Sub_Cat_Name=id)).order_by('id')
            serializer = NestedSubCategorySerializer(nested, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            nested=Sub_Sub_Categories.objects.all().order_by('id')
            serializer = NestedSubCategorySerializer(nested,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False,methods=['get'])
    def CategorySubCategory(self,request,id):
        nested = Main_Categories.objects.all().order_by('id')
        serializer = CategorySerializer(nested, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
