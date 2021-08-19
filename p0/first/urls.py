from django.urls import path
from .views import hw

urlpatterns = [
    path('', hw, name='index')
]