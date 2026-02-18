
from django.shortcuts import render, redirect

from cam_borrow.forms import SellerRegister, CameraRegister, LensRegister, AccessoryRegister
from cam_borrow.models import Seller, Camera, Lens, Accessory

# _______________________________________________________________________________
# SELLER
# _______________________________________________________________________________
def seller_profile(request):
    data=request.user
    seller_profile=Seller.objects.get(seller_detail=data.id)
    return render(request,'seller/seller_profile.html',{'data':seller_profile})

def seller_list(request):
    data=Seller.objects.all()
    return render(request,'seller/seller_list.html',{'data':data})



def seller_edit(request):
    user = request.user
    seller=Seller.objects.get(seller_detail=user.id)

    if request.method=='POST':
        seller_form =SellerRegister(request.POST,request.FILES, instance=seller)
        if seller_form.is_valid():
            seller_form.save()
            return redirect('seller_profile')
    else:
        seller_form =SellerRegister(instance=seller)
        return render(request,'seller/seller_edit.html',{'data':seller_form})

def seller_delete(request,id):
    seller_delete = Seller.objects.get(id=id)
    Seller.delete.delete()
    return redirect('seller_list')




def camera_add(request):
    form = CameraRegister()
    if request.method == "POST":
        form = CameraRegister(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_camera_list')
    return render(request, "seller/camera_add.html", {"form": form})


def lens_add(request):

    seller = Seller.objects.get(seller_detail=request.user)

    if request.method == "POST":
        form = LensRegister(request.POST, request.FILES)

        if form.is_valid():
            lens = form.save(commit=False)   # VERY IMPORTANT
            lens.seller = seller             # assign seller
            lens.save()
            return redirect('seller_lens_list')
    else:
        form = LensRegister()

    return render(request, 'seller/lens_add.html', {'form': form})

# -------------------------------
# Lens EDIT
# -------------------------------
def lens_edit(request, id):

    seller = Seller.objects.get(seller_detail=request.user)
    lens = Lens.objects.get(id=id, seller=seller)

    if request.method == "POST":
        form = LensRegister(request.POST, request.FILES, instance=lens)
        if form.is_valid():
            form.save()
            return redirect('seller_lens_list')
    else:
        form = LensRegister(instance=lens)

    return render(request, 'seller/lens_edit.html', {'form': form})

# -------------------------------
# Lens DELETE
# -------------------------------
def lens_delete(request, id):

    seller = Seller.objects.get(seller_detail=request.user)

    lens = Lens.objects.get(id=id, seller=seller)

    lens.delete()

    return redirect('seller_lens_list')

def accessory_add(request):

    seller = Seller.objects.get(seller_detail=request.user)

    if request.method == "POST":
        form = AccessoryRegister(request.POST, request.FILES)

        if form.is_valid():
            accessory = form.save(commit=False)  # save stop
            accessory.seller = seller            # assign seller
            accessory.save()                     # now save
            return redirect('seller_accessory_list')
    else:
        form = AccessoryRegister()

    return render(request, 'seller/accessory_add.html', {'form': form})


# def accessory_add(request):
#     form = AccessoryRegister()
#     if request.method == "POST":
#         form = AccessoryRegister(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('seller_camera_list')
#     return render(request, "seller/accessory_add.html", {"form": form})
#

def seller_camera_list(request):
    cameras = Camera.objects.filter(seller=request.user)

    context = {
        'cameras': cameras
    }

    return render(
        request,
        'seller/camera_list.html',
        context
    )

def seller_lens_list(request):
    seller = Seller.objects.get(seller_detail=request.user)

    lens = Lens.objects.filter(seller=seller)

    context = {
        'lens': lens
    }

    return render(
        request,
        'seller/lens_list.html',
        context
    )



def seller_accessory_list(request):
    seller = Seller.objects.get(seller_detail=request.user)

    accessory = Accessory.objects.filter(seller=seller)
    context = {
        'accessory': accessory
    }

    return render(
        request,
        'seller/accessory_list.html',
        context
    )
# -------------------------------
# Camera Add
# -------------------------------


def camera_add(request):

    seller = Seller.objects.get(seller_detail=request.user)

    if request.method == "POST":
        form = CameraRegister(request.POST, request.FILES)

        if form.is_valid():
            camera = form.save(commit=False)   # ❗ Don't save yet
            camera.seller = seller             # ✅ Assign seller
            camera.save()                      # ✅ Now save
            return redirect('seller_camera_list')

    else:
        form = CameraRegister()

    return render(request, 'seller/camera_add.html', {'form': form})


# -------------------------------
# CAMERA LIST
# -------------------------------
def seller_camera_list(request):
    cameras = Camera.objects.all()
    return render(request, 'seller/camera_list.html', {'cameras': cameras})


# -------------------------------
# CAMERA EDIT
# -------------------------------
def camera_edit(request, id):

    seller = Seller.objects.get(seller_detail=request.user)

    camera = Camera.objects.get(id=id, seller=seller)

    if request.method == "POST":
        form = CameraRegister(request.POST, request.FILES, instance=camera)
        if form.is_valid():
            form.save()
            return redirect('seller_camera_list')
    else:
        form = CameraRegister(instance=camera)

    return render(request, 'seller/camera_edit.html', {'form': form})


# -------------------------------
# CAMERA DELETE
# -------------------------------
def camera_delete(request, id):

    seller = Seller.objects.get(seller_detail=request.user)

    camera = Camera.objects.get(id=id, seller=seller)

    camera.delete()

    return redirect('seller_camera_list')

