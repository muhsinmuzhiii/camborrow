from django.contrib.auth import logout
from django.shortcuts import render, redirect

from cam_borrow.models import Seller, Customer, Lens, Camera, Accessory


def seller_bookings(request):
    seller = Seller.objects.get(seller_detail=request.user)

    bookings = Booking.objects.filter(
        camera__seller=seller
    ) | Booking.objects.filter(
        lens__seller=seller
    ) | Booking.objects.filter(
        accessory__seller=seller
    )

    return render(request, 'seller/seller_bookings.html', {'bookings': bookings})

def seller_list_admin(request):
    data=Seller.objects.all()
    return render(request,'admin/seller_list.html',{'data':data})

def customer_list_admin(request):
    data=Customer.objects.all()
    return render(request,'admin/customer_list.html',{'data':data})
def camera_list_admin(request):
    data=Camera.objects.all()
    return render(request,'admin/camera_list.html',{'data':data})

def lens_list_admin(request):
    data=Lens.objects.all()
    return render(request,'admin/lens_list.html',{'data':data})

def accessory_list_admin(request):
    data=Accessory.objects.all()
    return render(request,'admin/accessory_list.html',{'data':data})

def Log_out(request):
    logout(request)
    return redirect('index')