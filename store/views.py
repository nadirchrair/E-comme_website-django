from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
# Create your views here.

def index(request):
    product = Product.objects.all()
    context = {
    "product": product,
    }
    return render(request,'index.html',context)

def product_detial(request,slug):
    detial = Product.objects.get(slug=slug)
    context = {
    "detial": detial,
    }
    return render(request,'detial.html',context)


def add_cart(request,slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user ,order=False , product=product)
    if created :
        cart.order.add(order)
        cart.save()
    else :
        order.quantity+=1    
        order.save()
        
    return redirect (reverse("product_detial",kwargs={"slug":slug}))    

def cart(request):
    cart =get_object_or_404(Cart,user=request.user)
    context={
        "orders":cart.order.all()
    }
    return render(request,'cart.html',context)

def delete(request):
    cart = request.user.cart
    if cart :
        cart.order.all().delete()
        cart.delete()
    return redirect("index")    