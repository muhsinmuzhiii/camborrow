from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from cam_borrow.forms import SellerRegister, LoginRegister, CustomerRegister
from cam_borrow.models import Customer


# Create your views here.


def index(request):
    return render(request, 'index.html')

# dash

def dash(request):
    return render(request,'dash.html')




# base view
# ___________________________________________________

def Login(request):
    return render(request, 'login.html')


def admin(request):
    return render(request, 'admin/adminbase.html')


def seller(request):
    return render(request, 'seller/sellerbase.html')

def customer(request):
    return render(request, 'customer/customerbase.html')

# ___________________________________________________



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')  # safer get()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            elif user.is_customer:
                return redirect('customer')
            elif user.is_seller:
                return redirect('seller')
        else:
            messages.error(request, 'Username or password is incorrect')  # error level

    return render(request, 'login.html')



# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         # authenticate = inbuild fuction
#         if user is not None:
#             login(request, user)
#             if user.is_staff:
#                 return redirect('admin')
#             elif user.is_customer:
#                 return redirect('customer')
#             elif user.is_seller:
#                 return redirect('seller')
#         else:
#             messages.info(request, 'Username or password is incorrect')
#     return render(request, 'login.html')



def seller_add(request):
    if request.method == "POST":
        seller_form = SellerRegister(request.POST, request.FILES,request.FILES)
        login_form = LoginRegister(request.POST)



        if seller_form.is_valid() and login_form.is_valid():
           seller=login_form.save(commit=False)
           seller.is_seller = True
           seller.save()

           user =seller_form.save(commit=False)
           user.seller_detail = seller
           user.save()

    else:
           seller_form = SellerRegister()
           login_form = LoginRegister()
    return render(request, 'register.html',{'seller_form':seller_form,'login_form':login_form})

def customer_add(request):
    if request.method == "POST":
        customer_form = CustomerRegister(request.POST, request.FILES,request.FILES)
        login_form = LoginRegister(request.POST)



        if customer_form.is_valid() and login_form.is_valid():
           customer=login_form.save(commit=False)
           customer.is_customer = True
           customer.save()

           user =customer_form.save(commit=False)
           user.customer_detail = customer
           user.save()

    else:
           customer_form = CustomerRegister()
           login_form = LoginRegister()
    return render(request, 'register2.html',{'customer_form':customer_form,'login_form':login_form})


def customer_profile(request):
    data = request.user
    customer_profile =  Customer.objects.get(customer_detail_id=data.id)
    return render(request,"customer/customer_profile.html",{"data":customer_profile})