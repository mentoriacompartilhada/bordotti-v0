from django.urls import path
from .views import hw

urlpatterns = [
    path('hello', hw, name='index')
]
