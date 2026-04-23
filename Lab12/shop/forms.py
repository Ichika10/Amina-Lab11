# forms.py
from django import forms
from .models import Category, Product, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] # Поля из твоей модели

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'is_active']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating'] 
        # Поле product мы не включаем сюда, так как будем привязывать его автоматически во views