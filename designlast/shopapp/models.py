from django.db import models

# Slider
class Slider(models.Model):
    image = models.ImageField(upload_to = 'slider')
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    


# Color
class Color(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name



# Brand
class Brand(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name




# Category
class Category(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name



# Product
class Product(models.Model):
    name = models.CharField(max_length = 100)
    product_code = models.IntegerField(blank = True, null = True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank = True, null = True)
    discount_off_price = models.IntegerField(blank = True, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'product')
    order_now_link = models.URLField(max_length=200, blank=False)
    description = models.TextField()
    publish_on = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_on = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name
