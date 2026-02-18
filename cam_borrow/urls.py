from django.urls import path

from cam_borrow import views, castomerviews, sellerviews
from cam_borrow.models import Login
from cam_borrow.views import customer_profile

urlpatterns = [

 path("index", views.index, name="index"),
 path("Login", views.Login, name="Login"),
 path("admin", views.admin, name="admin"),
 path("seller", views.seller, name="seller"),
 path("customer", views.customer, name="customer"),
 path("login_view", views.login_view, name="login_view"),
 path("seller_add", views.seller_add, name="seller_add"),
 path("customer_add", views.customer_add, name="customer_add"),
 path("dash", views.dash, name="dash"),

 path("customer_profile", views.customer_profile, name="customer_profile"),
 path("customer_profile", castomerviews.customer_profile, name="customer_profile"),
 path("customer_list", castomerviews.customer_list, name="customer_list"),
 path("customer_edit", castomerviews.customer_edit, name="customer_edit"),
 path("customer_delete", castomerviews.customer_delete, name="customer_delete"),

 path("seller_camera_list", sellerviews.seller_camera_list, name="seller_camera_list"),
 path("seller_profile",sellerviews.seller_profile, name="seller_profile"),
 path("seller_list", sellerviews.seller_list, name="seller_list"),
 path("seller_edit",sellerviews.seller_edit, name="seller_edit"),
 path("seller_lens_list", sellerviews.seller_lens_list, name="seller_lens_list"),
 path("seller_accessory_list",sellerviews.seller_accessory_list, name="seller_accessory_list"),


 path('camera_add', sellerviews.camera_add, name="camera_add"),
 path('lens_add', sellerviews.lens_add, name="lens_add"),
 path('accessory_add', sellerviews.accessory_add, name="accessory_add"),
 path('lens_edit/<int:id>/', sellerviews.lens_edit, name="lens_edit"),
 path('lens_delete/<int:id>/', sellerviews.lens_delete, name="lens_delete"),


 path('camera_add/', sellerviews.camera_add, name='camera_add'),
 path('camera_list/', sellerviews.seller_camera_list, name='seller_camera_list'),
 path('camera_edit/<int:id>/', sellerviews.camera_edit, name='camera_edit'),
 path('camera_delete/<int:id>/', sellerviews.camera_delete, name='camera_delete'),
]