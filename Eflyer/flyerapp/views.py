from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    prod = Products.objects.filter(category="Fashion")
    food = Products.objects.filter(category="Food")
    elec = Products.objects.filter(category="Electronics")
    cose = Products.objects.filter(category="Cosmatics")
    
    context = {"prod":prod,"food":food,"elec":elec,"cose":cose}
    
    return render(request, 'index.html',context)

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def base(request):
    prod = Products.objects.all()
    
    context = {"prod":prod}
    return   render(request, 'buy.html',context)

@login_required(login_url='login')
def cart(request):
    incart = carte.objects.filter(usr_cos = request.user)
    
    total_items = incart.count()
    
    context = {"incart":incart,"total_items":total_items}
    return  render(request, 'cart.html',context)



def delic(request, pk):
    if request.method =="POST":
        item_to_delete = get_object_or_404(carte, id=pk)
        product_id = item_to_delete.products.id
        print(product_id)
        item_to_delete.delete()
        return redirect('cart')
    return  render(request, 'cart.html')



