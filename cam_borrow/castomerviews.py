from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from cam_borrow.forms import CustomerRegister
from cam_borrow.models import Customer, Camera, Lens, Accessory, Seller, Cart, Order


def coustomer_edit(request):

    user = request.user
    customer=Customer.objects.get(Customer_details=user)
    if request.method == "POST":
        customer_form = CustomerRegister(request.POST,request.FILES,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('coustomer_profile')
        else:
            customer_form = CustomerRegister(instance=customer)
        return render(request,'coustomer/coustomer_edit.html',{'data':customer_form})

def customer_delete(request,id):
    customer_delete = Customer.objects.get(id=id)
    Customer.delete.delete()
    return redirect('customer_list')

def camera_list(request):
    camera = Camera.objects.all()
    return render(request,'customer/camera_list.html',{'camera':camera})

def lens_list(request):
    lens = Lens.objects.all()
    return render(request,'customer/lens_list.html',{'lens':lens})

def accessory_list(request):
    accessory = Accessory.objects.all()
    return render(request,'customer/accessory_list.html',{'accessory':accessory})



def camera_view(request):
    camaras = Camera.objects.get(Camera_details=id)
    return render(request,'customer/camera_list.html',{'data':camaras})



def customer_profile(request):
    data = request.user
    customer_profile =  Customer.objects.get(customer_detail=data.id)
    return render(request,"customer/customer_profile.html",{"data":customer_profile})

def customer_list(request):
    data=Customer.objects.all()
    return render(request,'customer/customer_list.html',{'data':data})



def customer_edit(request):
    user = request.user
    customer=Customer.objects.get(customer_detail=user.id)

    if request.method=='POST':
        customer_form =CustomerRegister(request.POST,request.FILES, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer_profile')
    else:
        customer_form =CustomerRegister(instance=customer)
        return render(request,'customer/customer_edit.html',{'data':customer_form})

def customer_delete(request,id):
    customer_delete = Customer.objects.get(id=id)
    Customer.delete.delete()
    return redirect('customer_list')


def customer_index(request):
    cameras = Camera.objects.all().filter(available=True)
    lens = Lens.objects.all().filter(available=True)
    accessories = Accessory.objects.all().filter(available=True)

    return render(request,"customer/index.html",
    {
        'cameras': cameras,
        'lens': lens,
        'accessories': accessories,

    })


class Product:
    pass


def product_list(request):
    products = Product.objects.all()
    return render(request,'customer/product_list.html',{'products':products})

def add_cart(request, item_type,id):

    customer = Customer.objects.get(customer_detail=request.user)

    cart_item = Cart.objects.create(
        customer=customer,
        quantity=1
    )

    if item_type == 'camera':
        camera = Camera.objects.get(id=id)
        cart_item.camera = camera

    elif item_type == 'lens':
        lens = Lens.objects.get(id=id)
        cart_item.lens = lens

    elif item_type == 'accessory':
        accessory = Accessory.objects.get(id=id)
        cart_item.accessory = accessory

    cart_item.save()

    return redirect('cart_view')




def camera_view(request):
    cameras = Camera.objects.all()
    return render(request, "customer/camera_views.html", {"cameras": cameras})

def lens_view(request):
    lenses = Lens.objects.all()
    return render(request, "customer/lens_views.html", {"lenses": lenses})

def accessory_view(request):
    accessory = Accessory.objects.all()
    return render(request, "customer/accessory_views.html", {"accessory":accessory})

def customer_accessory_list(request):
    data=Accessory.objects.all()
    return render(request,"customer/accessory_views.html",{'data':data})



def view_cart(request):
    customer = Customer.objects.get(customer_detail=request.user)
    items = Cart.objects.filter(customer=customer)

    total = 0
    for item in items:
        if item.lens:
            total += item.lens.rent_per_day * item.quantity
        elif item.camera:
            total += item.camera.rent_per_day * item.quantity
        elif item.accessory:
            total += item.accessory.rent_per_day * item.quantity

    return render(request, 'customer/cart.html', {
        'items': items,
        'total': total
    })
    return render(request, 'customer/cart.html', {'items': items})
def cart_view(request):
    customer = Customer.objects.get(customer_detail=request.user)
    items = Cart.objects.filter(customer=customer)

    total = 0

    for i in items:
        if i.camera:
            total += i.camera.rent_per_day * i.quantity
        elif i.lens:
            total += i.lens.rent_per_day * i.quantity
        elif i.accessory:
            total += i.accessory.rent_per_day * i.quantity

    return render(request, "customer/cart.html", {
        'items': items,
        'total': total

    })

def remove_cart(request, id):
    customer = Customer.objects.get(customer_detail=request.user)

    item = Cart.objects.filter(id=id, customer=customer).first()

    if item:
        item.delete()

    return redirect('cart_view')



def checkout(request):
    customer = Customer.objects.get(user=request.user)
    items = Cart.objects.filter(customer=customer)

    total = 0
    for i in items:
        if i.camera:
            total += i.camera.rent_per_day
        elif i.lens:
            total += i.lens.rent_per_day
        elif i.accessory:
            total += i.accessory.rent_per_day

    return render(request, "customer/checkout.html", {
        'items': items,
        'total': total
    })

def add_camera_to_cart(request, id):
    customer = Customer.objects.get(user=request.user)
    camera = Camera.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        customer=customer,
        camera=camera
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')

def add_lens_to_cart(request, id):
    customer = Customer.objects.get(customer_detail=request.user)
    lens = Lens.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        customer=customer,
        lens=lens
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


def add_accessory_to_cart(request, id):
    customer = Customer.objects.get(customer_detail=request.user)
    accessory = Accessory.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        customer=customer,
        accessory=accessory
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')

def cart_plus(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

def cart_minus(request, id):
    cart_item = Cart.objects.get(id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_view')

def cart_remove(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('cart_view')



def book_now(request):

    customer = Customer.objects.get(customer_detail=request.user)
    cart_items = Cart.objects.filter(customer=customer)

    for item in cart_items:

        if item.camera:
            if item.camera.stock >= item.quantity:
                item.camera.stock -= item.quantity
                item.camera.save()
            else:
                messages.error(request, f"{item.camera.camera_name} not available")
                return redirect('cart_view')

        elif item.lens:
            if item.lens.stock >= item.quantity:
                item.lens.stock -= item.quantity
                item.lens.save()
            else:
                messages.error(request, f"{item.lens.lens_name} not available")
                return redirect('cart_view')

        elif item.accessory:
            if item.accessory.stock >= item.quantity:
                item.accessory.stock -= item.quantity
                item.accessory.save()
            else:
                messages.error(request, f"{item.accessory.accessory_name} not available")
                return redirect('cart_view')

    # 🔥 Clear cart after booking
    cart_items.delete()

    messages.success(request, "Booking Successful!")
    return redirect('cart_view')


# buy cart


def buy_cart(request):
    # 🔐 Check login
    if not request.user.is_authenticated:
        messages.error(request, "Please login first!")
        return redirect("login")

    # 👤 Get customer
    try:
        customer = Customer.objects.get(customer_detail=request.user)
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found!")
        return redirect("index")

    # 🛒 Get cart items
    cart_items = Cart.objects.filter(customer=customer)

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty!")
        return redirect("cart_view")

    # 🔄 Create orders
    for item in cart_items:
        Order.objects.create(
            customer=customer,
            camera=item.camera,
            lens=item.lens,
            accessory=item.accessory,
            quantity=item.quantity
        )

    # 🗑 Clear cart after ordering
    cart_items.delete()

    messages.success(request, "Order placed successfully!")
    return redirect("view_orders")  # change to your order page name


def view_orders(request):
    customer = Customer.objects.get(customer_detail=request.user)
    orders = Order.objects.filter(customer=customer)

    return render(request, "customer/view_orders.html", {
        "orders": orders
    })

from django.shortcuts import render, redirect
from .models import Order, Customer

def customer_orders(request):

    if not request.user.is_authenticated:
        return redirect("login")

    # 🔥 Get Customer instance properly
    customer = Customer.objects.get(customer_detail=request.user)

    # 🔥 Now filter using Customer object
    orders = Order.objects.filter(customer=customer).order_by("-ordered_on")

    return render(request, "customer/customer_orders.html", {"orders": orders})
def Logout(request):
    logout(request)
    return redirect('index')