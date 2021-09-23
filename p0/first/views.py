# from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PessoaSerializer

def hw(request):
    return HttpResponse('Hello World')


class PessoaView(ListAPIView,CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaViewOps(RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


pessoa = PessoaView.as_view()
pessoaops = PessoaViewOps.as_view()