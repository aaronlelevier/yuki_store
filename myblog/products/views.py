import datetime
import re
import random
from time import gmtime, strftime

from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Template, Context, RequestContext, loader
from django.contrib import auth 
from django.contrib.auth.models import User 
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail, EmailMessage

# EmailMessage Imports
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.template import Context
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.forms.formsets import formset_factory

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# my modules
from products.models import Product, Category, Color, EmailSignup, Style
from forms import EmailSignupForm


class IndexView(FormView):
	form_class = EmailSignupForm
	template_name = 'products/index2.html'
	success_url = reverse_lazy('products:index') 

	def form_valid(self, form):
		email = form.cleaned_data['email']
		EmailSignup.objects.create(email=email)
		return super(IndexView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['main_slider'] = Product.objects.all()[:9]
		context['categories'] = Category.objects.all()
		context['latest_products'] = Product.objects.order_by('-date')[:3]
		context['best_seller'] = Product.objects.filter(best_seller=True)[:3]
		context['ad_banner'] = Product.objects.order_by('date')[:2]
		context['popular_styles'] = Style.objects.order_by('name')
		return context