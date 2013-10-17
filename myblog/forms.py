from django import forms
from django.contrib.auth.models import User

from products.models import Product, Category, Color, EmailSignup, Style


class EmailSignupForm(forms.ModelForm):
	class Meta:
		model = EmailSignup
    	fields = ('email',)
