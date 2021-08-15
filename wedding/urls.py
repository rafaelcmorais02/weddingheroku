from django.urls import path
from .views import convidadoAPIView, convidadosDetail

urlpatterns = [
    path('api/', convidadoAPIView.as_view()),
    path('api/<int:id>/', convidadosDetail.as_view()),
]