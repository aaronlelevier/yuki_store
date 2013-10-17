from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from products.models import Product, Category, Color, EmailSignup, Style


class ProductForm(forms.ModelForm):
	description = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
	class Meta:
		model = Product

class ProductAdmin(admin.ModelAdmin):
	form = ProductForm
	filter_horizontal = ('color', 'style',)
	exclude = ('slug',)
	list_display = ('name', 'category', 'best_seller', 'index_picture')
	list_filter = ('name', 'category', 'best_seller', 'index_picture')

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category

class CategoryAdmin(admin.ModelAdmin):
	form = CategoryForm
	exclude = ('slug',)

class ColorForm(forms.ModelForm):
	class Meta:
		model = Color

class ColorAdmin(admin.ModelAdmin):
	form = ColorForm
	exclude = ('slug',)

class StyleForm(forms.ModelForm):
	class Meta:
		model = Style

class StyleAdmin(admin.ModelAdmin):
	form = StyleForm
	exclude = ('slug',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(EmailSignup)
