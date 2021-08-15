from django.db.models import fields
from rest_framework import serializers
from .models import Convidados
class ConvidadoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Convidados
        fields = '__all__'