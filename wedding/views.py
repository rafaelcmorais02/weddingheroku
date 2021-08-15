from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Convidados
from .serializer import ConvidadoSerializer

class convidadoAPIView(APIView):
    def get(self, request):
        convidados = Convidados.objects.all()
        serializer = ConvidadoSerializer(convidados, many = True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serialier = ConvidadoSerializer(data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data, status.HTTP_201_CREATED)
        return Response(serialier.errors, status.HTTP_400_BAD_REQUEST)

class convidadosDetail(APIView):
    def get_check(self, id):
        return Convidados.objects.filter(id=id).exists()

    def get(self, request, id):
        status_convidados = self.get_check(id)
        if status_convidados == True:
            convidados = Convidados.objects.get(id=id)
            serializer = ConvidadoSerializer(convidados)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        status_convidados = self.get_check(id)
        if status_convidados == True:
            convidados = Convidados.objects.get(id=id)
            serialier = ConvidadoSerializer(convidados, request.data)
            if serialier.is_valid():
                serialier.save()
                return Response(serialier.data)
            return Response(serialier.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        status_convidados = self.get_check(id)
        if status_convidados == True:
             convidados = Convidados.objects.get(id=id)
             convidados.delete()
             return Response(status.HTTP_204_NO_CONTENT)
        else:
            return Response(status.HTTP_404_NOT_FOUND)