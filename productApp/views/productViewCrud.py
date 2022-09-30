from rest_framework.response import Response
from rest_framework.decorators import api_view
from productApp.models import Product
from productApp.serializers import ProductSerializer

@api_view(['GET','POST'])
def product_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        product_serializer = ProductSerializer(product,many=True)
        return Response(product_serializer.data)

    elif request.method == 'POST':
        product_serializer = ProductSerializer(data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def product_detail_view(request,pk=None):
    
    if request.method == 'GET':
        product = Product.objects.filter(id = pk).first()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)

    elif request.method == 'PUT':
       product = Product.objects.filter(id = pk).first() 
       product_serializer = ProductSerializer(instance=product, data = request.data)
       if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)

    elif request.method == 'DELETE':
        product = Product.objects.filter(id = pk).first()
        product.delete()
        return Response("Eliminado...")