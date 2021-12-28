

from django.contrib import admin
from django.urls import path
# from django.http import request
from .views import update,delet,send

urlpatterns = [
    path('update/<int:id>/<str:text>/',update),
    path('delete/<int:id>/',delet),
    path('send/<int:id>/<int:note>/',send)

]