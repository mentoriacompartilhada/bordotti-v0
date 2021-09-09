from django.urls import path
from .views import hw, pessoa

urlpatterns = [
    path('hello/', hw, name='hello'),
    path('pessoa/', pessoa, name='list_pessoa')
]
