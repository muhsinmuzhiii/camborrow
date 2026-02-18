from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_seller =models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


    # seller

class Seller(models.Model):
    seller_detail = models. OneToOneField("Login", on_delete=models.CASCADE)
    shop_name = models.CharField( max_length=100)
    phone =models.CharField( max_length=100)
    address =models.TextField()
    email = models.EmailField()
    id_proof = models.FileField(upload_to='documents/')
    # is_approved = models.BooleanField(default=False)
    #
    # joined_on = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    customer_detail = models. OneToOneField("Login", on_delete=models.CASCADE)
    name = models.CharField( max_length=100)
    phone =models.CharField( max_length=100)
    address =models.TextField()
    email = models.EmailField()
    profile_pic = models.FileField(upload_to='documents/')
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Camera(models.Model):
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)

    camera_name = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=100)

    BRAND_CHOICES = (
        ("CANON", "Canon"),
        ("SONY", "Sony"),
        ("NIKON", "Nikon"),
        ("PANASONIC", "Panasonic"),
        ("FUJIFILM", "Fujifilm"),
    )
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)

    TYPE_CHOICES = (
        ("DSLR", "DSLR"),
        ("MIRRORLESS", "Mirrorless"),
        ("CINEMA", "Cinema Camera"),
        ("ACTION", "Action Camera"),
    )
    camera_type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    resolution = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)

    rent_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    image = models.ImageField(upload_to="camera_images/")
    document = models.FileField(upload_to="camera_docs/")

    is_available = models.BooleanField(default=True)

    def _str_(self):
        return self.camera_name



class Lens(models.Model):
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)

    lens_name = models.CharField(max_length=100)

    LENS_TYPE = (
        ("PRIME", "Prime"),
        ("ZOOM", "Zoom"),
        ("WIDE", "Wide Angle"),
        ("TELE", "Telephoto"),
        ("MACRO", "Macro"),
    )
    lens_type = models.CharField(max_length=50, choices=LENS_TYPE)

    mount_type = models.CharField(max_length=50)
    focal_length = models.CharField(max_length=50)

    rent_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    image = models.ImageField(upload_to="lens_images/")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.lens_name




class Accessory(models.Model):
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)

    accessory_name = models.CharField(max_length=100)

    CATEGORY = (
        ("TRIPOD", "Tripod"),
        ("GIMBAL", "Gimbal"),
        ("MIC", "Microphone"),
        ("LIGHT", "Lighting Kit"),
        ("BATTERY", "Battery"),
        ("BAG", "Camera Bag"),
    )
    category = models.CharField(max_length=50, choices=CATEGORY)

    brand = models.CharField(max_length=50)

    rent_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    image = models.ImageField(upload_to="accessory_images/")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.accessory_name