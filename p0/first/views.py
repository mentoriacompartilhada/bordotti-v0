# from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,   DestroyAPIView, RetrieveAPIView
from .base_view import CreateAPIView, UpdateAPIView
from .serializers import PessoaSerializer

def hw(request):
    return HttpResponse('Hello World')


class PessoaView(ListAPIView, CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaViewR(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer



pessoa = PessoaView.as_view()
pessoa2 = PessoaViewR.as_view()