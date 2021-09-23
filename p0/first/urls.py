from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import hw, pessoa,pessoaops

urlpatterns = [
    path('hello', hw, name='hello'),
    path('pessoas', pessoa, name='list_pessoa'),
    path('pessoas/<int:pk>', pessoaops, name='ops_pessoa')
]

urlpatterns = format_suffix_patterns(urlpatterns)
