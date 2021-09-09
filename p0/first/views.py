# from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import PessoaSerializer

def hw(request):
    return HttpResponse('Hello World')


class PessoaView(ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


pessoa = PessoaView.as_view()