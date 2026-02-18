from django.shortcuts import render, redirect

from cam_borrow.forms import CustomerRegister
from cam_borrow.models import Customer


def customer_profile(request):
    data=request.user
    customer_profile=Customer.objects.get(customer_detail=data.id)
    return render(request,'customer/customer_profile.html',{'data':customer_profile})

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
    customer_delete=Customer.objects.get(id=id)
    customer_delete.delete()
    return redirect('customer_list')
