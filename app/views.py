from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response

from app.serializers import *

class Productcrud(APIView):
    def get(self,request,id):
        PDO=Product.objects.all()
        #PDO=Product.objects.get(id=id)
        PJO=Serializerproduct(PDO,many=True)
        #PJO=Serializerproduct(PDO)
        return Response(PJO.data)


    def post(self,request,id):
        JDO=request.data
        PDO=Serializerproduct(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'Error':'Data is not inserted'})

    def put(self,request,id):
        PO=Product.objects.get(id=id)
        PDO=Serializerproduct(PO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is updated successfully'})
        else:
            return Response({'Error':'Data is not updated'})
    
    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        PDO=Serializerproduct(PO,data=request.data,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is updated successfully'})
        else:
            return Response({'Error':'Data is not updated'})
    
    def delete(self,request,id):
        PO=Product.objects.get(id=id).delete()
        return Response({'value':'data deleted suceesfully'})