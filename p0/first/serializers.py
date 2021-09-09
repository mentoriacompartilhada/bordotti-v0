from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        #exclude = ['password']
        fields = '__all__'