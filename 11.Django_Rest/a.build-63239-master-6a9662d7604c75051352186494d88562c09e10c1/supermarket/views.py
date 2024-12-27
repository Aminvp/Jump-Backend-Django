from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['POST'])
def create_product(request):
    name = request.data['name']  # Your codes
    price = request.data['price']
    product = Product.objects.create(name=name, price=price)
    response = {"message": "new product added successfully", "product": {"name": product.name, "price": product.price}}
    return Response(
        data=response  # return message & product details
    , status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product(request, product_id):
    if request.method == 'GET':  # Your codes
        product = Product.objects.get(id=product_id)
        response = {"name": product.name, "price": product.price}
        return Response(
            data=response  # return product details
        , status=status.HTTP_200_OK)
