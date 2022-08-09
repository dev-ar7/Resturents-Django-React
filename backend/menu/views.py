from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *



class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()


class CityViewSet(viewsets.ModelViewSet):

    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class CityCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CityCategorySerializer

    def get_queryset(self):
        return CityCategory.objects.all()


class ResturantViewSet(viewsets.ModelViewSet):

    serializer_class = ResturantSerializer

    def get_queryset(self):
        return Resturant.objects.all()


class ResturantCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ResturantCategorySerializer

    def get_queryset(self):
        return ResturantCategory.objects.all()


class MenuviewSet(viewsets.ModelViewSet):

    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()