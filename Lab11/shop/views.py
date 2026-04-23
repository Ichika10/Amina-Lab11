from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Басты парақша (санаттар тізімі)
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

# Каталог (тауарлар тізімі)
def catalog(request):
    products = Product.objects.all() 
    return render(request, 'catalog.html', {'products': products})

# Тауардың толық сипаттамасы
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) 
    return render(request, 'detail.html', {'product': product})