from django.shortcuts import render,redirect
from .models import ProductModel
from .forms import ProductForm
from django.contrib import messages

# Create your views here.


def AddProduct(request):  # sourcery skip: extract-method
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'GET':
        form = ProductForm()
    else:
        form = ProductForm(request.POST)
        if form.is_valid():            
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            weight = form.cleaned_data['weight']
            product = ProductModel(name = name, price = price,weight = weight)
            product.save(using='product_db')
            messages.success(request , 'Post added successfully')

            return redirect('showproduct')
    return render(request, 'addproduct.html', {'form': form,'title':'Add Product'})


def ShowProduct(request):
    if not request.user.is_authenticated:
        return redirect('login')
    products = ProductModel.objects.using('product_db').all()
    return render(request, 'showproduct.html', {'products':products})
    