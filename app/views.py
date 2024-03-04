from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response

from app.serializers import *

class Productcrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJO=Serializerproduct(PDO,many=True)
        return Response(PJO.data)


    def post(self,request):
        JDO=request.data
        PDO=Serializerproduct(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'Error':'Data is not inserted'})