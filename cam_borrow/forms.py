from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

from cam_borrow.models import Login, Seller, Customer, Camera, Lens, Accessory


class LoginRegister(UserCreationForm):
    username = models.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confim password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class SellerRegister(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('shop_name','phone','address','id_proof',)


class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','phone','address','email','profile_pic',)
      # ------------------------------------------------------------------
      # camera form
    # ------------------------------------------------------------------


class CameraRegister(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ('camera_name','camera_model','brand','camera_type','resolution','sensor','rent_per_day','image')

 # ------------------------------------------------------------------
      # lens form
    # ------------------------------------------------------------------

class LensRegister(forms.ModelForm):
    class Meta:
        model = Lens
        fields = ('lens_name','lens_type','mount_type','focal_length','rent_per_day','image')


 # ------------------------------------------------------------------
      # lens form
    # ------------------------------------------------------------------



class AccessoryRegister(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ('accessory_name','category','brand','rent_per_day','image')