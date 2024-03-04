from rest_framework import serializers

from app.models import *

class Serializerproduct(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'