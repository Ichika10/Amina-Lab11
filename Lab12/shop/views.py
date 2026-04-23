from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm, ReviewForm

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

# 1. Жаңа санат қосу (GET және POST өңдеу)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid(): # Валидация (серверлік тексеріс) 
            form.save() # Дерекқорға сақтау 
            return redirect('home') # Санаттар тізіміне қайтару 
    else:
        form = CategoryForm() # Бос форма 
    return render(request, 'add_category.html', {'form': form})

# 2. Жаңа өнім қосу
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# 3. Белгілі бір өнімге пікір қалдыру [cite: 12]
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product # Пікірді нақты тауарға байлаймыз
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'product': product})