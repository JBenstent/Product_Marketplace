# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product

def index(request):


    # People.objects.create(first_name="Jon", last_name="Benstent")
    # people = People.objects.all()

    # Product.objects.create(name="Hose", description="For watering things", price="$14.00")

    products = Product.objects.all()

    context = {
    'products': products
    }


    return render(request, "index.html", context)

def create_user(request):

    if request.method == "POST":
        print ('*'*50)
        print (request.POST)
        print ('*'*50)
        # request.session['first_name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')


def product(request, id):

    product = Product.objects.get(id=id)
    product.save()

    context = {
    'product': product
    }

    return render(request, 'product.html', context)

def edit(request, id):

    product = Product.objects.get(id=id)

    context = {
    'product': product
    }

    return render(request, 'edit.html', context)

def update(request, id):

    if request.method == "POST":
        Product.objects.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        return redirect('/')
    else:
        return redirect('update/'+ str(id))

def remove(request, id):

    product = Product.objects.get(id=id)
    product.save()
    product.delete()

    return redirect('/')

def add_product(request):

    return render(request, 'add_product.html')

def create(request):

    Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])

    return redirect('/')
