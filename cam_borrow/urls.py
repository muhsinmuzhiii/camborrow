from django.urls import path

from cam_borrow import views, castomerviews, sellerviews, adminviews
from cam_borrow.models import Login


urlpatterns = [

 path("", views.index, name="index"),
 path("Login", views.Login, name="Login"),
 path("admin", views.admin, name="admin"),
 path("seller", views.seller, name="seller"),
 path("customer", views.customer, name="customer"),
 path("login_view", views.login_view, name="login_view"),
 path("seller_add", views.seller_add, name="seller_add"),
 path("customer_add", views.customer_add, name="customer_add"),
 path("dash", views.dash, name="dash"),



 path("customer_list", castomerviews.customer_list, name="customer_list"),
 path('customer_accessory_list',castomerviews.customer_accessory_list, name='customer_accessory_list' ),
 path("customer_delete", castomerviews.customer_delete, name="customer_delete"),

      # seller
 path("seller_camera_list", sellerviews.seller_camera_list, name="seller_camera_list"),
 path("seller_profile",sellerviews.seller_profile, name="seller_profile"),
 path("seller_list", sellerviews.seller_list, name="seller_list"),
 path("seller_edit",sellerviews.seller_edit, name="seller_edit"),
 path("seller_lens_list", sellerviews.seller_lens_list, name="seller_lens_list"),
 path("seller_accessory_list",sellerviews.seller_accessory_list, name="seller_accessory_list"),
 # path('seller_booking', sellerviews.seller_bookings,name='seller_booking'),
 # path('add-lens/<int:id>', castomerviews.add_lens_to_cart,name='add_lens_to_cart'),


 path('lens_add', sellerviews.lens_add, name="lens_add"),

 path('lens_edit/<int:id>/', sellerviews.lens_edit, name="lens_edit"),
 path('lens_delete/<int:id>/', sellerviews.lens_delete, name="lens_delete"),


 path('camera_add', sellerviews.camera_add, name='camera_add'),
 path('camera_list', sellerviews.seller_camera_list, name='seller_camera_list'),
 path('camera_edit/<int:id>/', sellerviews.camera_edit, name='camera_edit'),
 path('camera_delete/<int:id>/', sellerviews.camera_delete, name='camera_delete'),

 path('accessory_add', sellerviews.accessory_add, name="accessory_add"),
 path('accessory_edit/<int:id>/', sellerviews.accessory_edit, name="accessory_edit"),
 path('accessory_delete/<int:id>/', sellerviews. accessory_delete, name="accessory_delete"),



 path("accept-order/<int:id>/", sellerviews.accept_order, name="accept_order"),
 path("reject-order/<int:id>/", sellerviews.reject_order, name="reject_order"),
 path("seller-orders/", sellerviews.seller_orders, name="seller_orders"),
 # path('camera_view', castomerviews.camera_view, name='camera_view'),


    # customer
 path('customer_index',castomerviews.customer_index,name='customer_index'),
 path('customer_profile', castomerviews.customer_profile, name='customer_profile'),
 path('customer_list', castomerviews.customer_list, name='customer_list'),
 path('customer_edit', castomerviews.customer_edit, name='customer_edit'),
 path('customer_delete', castomerviews.customer_delete, name='customer_delete'),
 path('add_cart/<str:item_type>/<int:id>/', castomerviews.add_cart, name='add_cart'),

 path('cart_view', castomerviews.cart_view, name='cart_view'),
 path('camera_view', castomerviews.camera_view, name='camera_view'),
 path('lens_view', castomerviews.lens_view, name='lens_view'),

 path('checkout', castomerviews.checkout, name='checkout'),
 path('add_camera_to_cart/<int:id>/',castomerviews.add_camera_to_cart, name='add_camera_to_cart'),
 path('add_lens_to_cart/<int:id>/', castomerviews.add_lens_to_cart, name='add_lens_to_cart'),
 path('add_accessory_to_cart/<int:id>/', castomerviews.add_accessory_to_cart, name='add_accessory_to_cart'),
 path('cart_plus/<int:id>/', castomerviews.cart_plus, name='cart_plus'),
 path('cart_minus/<int:id>/', castomerviews.cart_minus, name='cart_minus'),
 path('cart_remove/<int:id>/', castomerviews.cart_remove, name='cart_remove'),
 path('remove_cart/<int:id>/', castomerviews.remove_cart, name='remove_cart'),
 path('buy-cart/', castomerviews.buy_cart, name='buy_cart'),
 path('customer_orders', castomerviews.customer_orders, name='customer_orders'),
 # path('accessory_view', castomerviews.accessory_view, name='accessory_view'),
 path('view_orders', castomerviews.view_orders, name='view_orders'),
 path('seller_list_admin', adminviews.seller_list_admin, name='seller_list_admin'),
 path('customer_list_admin', adminviews.customer_list_admin, name='customer_list_admin'),
 path("camera_list_admin", adminviews.camera_list_admin, name='camera_list_admin'),
 path('lens_list_admin', adminviews.lens_list_admin, name='lens_list_admin'),
 path('accessory_list_admin', adminviews.accessory_list_admin, name='accessory_list_admin'),
 path('cart_view', castomerviews.view_cart, name='cart_view'),
 path('book-now', castomerviews.book_now, name='book_now'),
 path('Log_out',adminviews.Log_out, name='Log_out'),
 path('Logout',castomerviews.Logout, name='Logout'),
 path('Log__out',sellerviews.Log__out, name='Log__out'),

]


