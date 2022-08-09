from rest_framework import serializers
from .models import *


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            'location_id', 'country', 'state', 'slug',
            'enabled', 'created'
        ]


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [
            'city_id', 'location', 'city', 'slug',
            'url', 'enabled', 'created'
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'category_id', 'category', 'slug',
            'enabled', 'created'
        ]


class CityCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CityCategory
        fields = [
            'city_category_id', 'city', 'category'
        ]


class ResturantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resturant
        fields = [
            'resturant_id', 'city', 'resturant', 'resturant_type',
            'address_locality', 'address_region', 'postal_code', 
            'address_country', 'street_address', 'phone', 'rating',
            'review_count', 'opening_hours', 'url', 'status', 
            'description', 'created', 'updated'
        ]


class ResturantCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ResturantCategory
        fields = [
            'resturant_category_id', 'category', 'resturant'
        ]


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'menu_id', 'resturant', 'menu', 'description',
            'price', 'currency', 'status', 'resturant_url',
            'created', 'updated'
        ]