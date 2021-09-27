from django.urls import path
from .views import hw, pessoa, pessoa2

urlpatterns = [
    path('hello', hw, name='hello'),
    path('pessoas', pessoa, name='list_pessoa'),
    path('pessoas/<int:pk>', pessoa2, name='list_pessoa')
]
