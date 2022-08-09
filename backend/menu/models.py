from django.db import models
import uuid


class Location(models.Model):

    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=120, null=True)
    state = models.CharField(max_length=120, null=True)
    slug = models.CharField(max_length=120, null=True)
    edabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foodie.location <Id:{self.location_id}> <State:{self.state}>"

    class Meta:
        db_table = "Foodie_location"
        verbose_name_plural = "Location"


class City(models.Model):

    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    city = models.CharField(max_length=120, null=True)
    slug = models.CharField(max_length=120, null=True)
    url = models.URLField(max_length=175, null=False)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foodie.city <Id:{self.city_id} <City:{self.city}>"

    class Meta:
        db_table = "Foodie_city"
        verbose_name_plural = "City"
        indexes = [models.indexes.Index(fields=["url"])]


class Category(models.Model):

    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=175, null=True)
    slug = models.CharField(max_length=120, null=True)
    enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foodie.category <Id:{self.category_id} <Name:{self.category}>"

    class Meta:
        db_table = "Foodie_category"
        verbose_name_plural = "Category"


class CityCategory(models.Model):

    city_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Foodie_city_category <City:{self.city}> <Category:{self.category}>"

    class Meta:
        db_table = "Foodie_city_category"
        verbose_name_plural = "CityCategory"


class Resturant(models.Model):

    resturant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    resturant = models.CharField(max_length=175, null=True, blank=True)
    resturant_type = models.CharField(max_length=175, null=True, blank=True)
    address_locality = models.CharField(max_length=220, null=True, blank=True)
    address_region = models.CharField(max_length=220, null=True, blank=True)
    postal_code = models.CharField(max_length=125, null=True, blank=True)
    address_country = models.CharField(max_length=220, null=True, blank=True)
    street_address = models.CharField(max_length=220, blank=True, null=True)
    phone = models.CharField(max_length=220, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    review_count = models.CharField(max_length=220, null=True, blank=True)
    opening_hours = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=255, null=False)
    status = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foodie.restaurant <Id:{self.restaurant_id}> <Name:{self.restaurant}>"

    class Meta:
        db_table = "Foodie_restaurant"
        verbose_name_plural = "Restaurant"
        indexes = [models.indexes.Index(fields=["url"])]


class ResturantCategory(models.Model):

    resturant_category_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    resturant = models.ForeignKey(Resturant, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Foodie.restaurant_category <Category:{self.category}> <Resturant:{self.resturant}>"

    class Meta:
        db_table = "Foodie_restaurant_category"
        verbose_name_plural = "RestaurantCategory"


class Menu(models.Model):

    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resturant = models.ForeignKey(Resturant, on_delete=models.RESTRICT)
    menu = models.CharField(max_length=220, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(max_length=155, null=True, default=0.0)
    currency = models.CharField(max_length=5, default="INR", null=True)
    status = models.BooleanField(default=True)
    resturant_url = models.URLField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foodie.menu <Id:{self.menu_id}> <Name:{self.menu}>"

    class Meta:
        db_table = "Foodie_menu"
        verbose_name_plural = "Menu"




