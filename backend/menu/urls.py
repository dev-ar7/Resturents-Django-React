from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r"location", LocationViewSet, basename="location"),
router.register(r"city", CityViewSet, basename="city"),
router.register(r"category", CategoryViewSet, basename="category"),
router.register(r"city-category", CityCategoryViewSet, basename="city-category"),
router.register(r"resturant", ResturantViewSet, basename="resturant"),
router.register(r"resturant-category", ResturantCategoryViewSet, basename="resturant-category"),
router.register(r"menu", MenuviewSet, basename="menu"),

urlpatterns = [
    path("", include(router.urls)),
]