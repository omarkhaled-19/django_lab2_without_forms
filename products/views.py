from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from products.models import techProducts

# Create your views here.

def productspage(request):
    return render(request,'index.html')

def landingpage(request):
    return render(request,'landing.html')

def test_layout(request):
    return render(request,'layouts/base.html')

# def test_file(request):
#     products = [
#          {"name": "Dell Laptop", "price": 2000, "category": "Laptops"},
#         {"name": "Samsung Phone", "price": 1000, "category": "Phones"},
#         {"name": "Dark Souls", "price": 500, "category": "Games"},
#         {"name": "Hp Laptop", "price": 800, "category": "Laptops"},
#     ]
#     return render(request,'test.html',context={'products':products})

def all_products(request):
    products = techProducts.objects.all()
    return render(request,'all.html',context={'products':products})

def show_product(request,product_id):
    product = get_object_or_404(techProducts,id=product_id)
    return render(request,'show.html',context={'product':product})

def delete_product(request,product_id):
    product = get_object_or_404(techProducts,id=product_id)
    product.delete()
    return redirect('../all')

def create_product(request):
    print(request)
    if request.method == 'POST':


        pname = request.POST.get('name')
        pprice = request.POST.get('price')
        pinstock = request.POST.get('instock')
        pdescription = request.POST.get('description')
        pimage = request.FILES.get('image')

        product = techProducts()
        product.name = pname
        product.price = pprice
        product.instock = pinstock
        product.description = pdescription
        product.image = pimage

        product.save()
        return redirect('/products/all')
    
    return render(request,'create.html')


