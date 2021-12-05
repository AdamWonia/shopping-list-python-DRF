from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShopList
from .serializer import ShopListSerializer


# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Shop List': '/product-list/',
        'Detail View': '/product-detail/<int:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:pk>/',
        'Delete': '/product-delete/<int:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def product_list(request):
    products = ShopList.objects.all()
    serializer = ShopListSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk=None):
    product = ShopList.objects.get(id=pk)
    serializer = ShopListSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ShopListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def product_update(request, pk=None):
    product = ShopList.objects.get(id=pk)
    serializer = ShopListSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def product_delete(request, pk=None):
    product = ShopList.objects.get(id=pk)
    product.delete()

    return Response('Item deleted!')
