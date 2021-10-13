from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .models import User
from .serializers import ProductSerializer
import random
from rest_framework.views import APIView

from .producer import publish

class ProductViewSet(viewsets.ViewSet):
    # list products  GET /products/
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data)

    #create a new product  POST /products
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    # get product, pk is primary key GET /products/<str:pk>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # delete products DELETE /products/<str:pk>
    def delete(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update products UPDATE /products/<str:pk>
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id':user.id
        })
