from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.core.validators import MaxLengthValidator
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
	name = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
	slug = models.SlugField(max_length=100, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('products.views.category', args=[str(self.id), self.slug])

	# class Meta:
	# 	ordering = ['name']


class Color(models.Model):
	name = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
	slug = models.SlugField(max_length=100, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Color, self).save(*args, **kwargs)

	class Meta:
		ordering = ['name']



def content_file_name(instance, filename):
	return '/'.join(['content', filename])

def style_file_name(instance, filename):
	return '/'.join(['style', filename])


class Style(models.Model):
	name = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
	slug = models.SlugField(max_length=100, blank=True)
	picture = models.FileField(upload_to=style_file_name, blank=True, verbose_name="Image")

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Style, self).save(*args, **kwargs)

	class Meta:
		ordering = ['name']


class Product(models.Model):
	name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
	category = models.ForeignKey(Category)
	color = models.ManyToManyField(Color)
	style = models.ManyToManyField(Style)
	description = models.TextField(max_length=2000, blank=True, validators=[MaxLengthValidator(2000)])
	picture = models.FileField(upload_to=content_file_name, null=False, verbose_name="Image", help_text="Regular product image")
	picture2 = models.FileField(upload_to=content_file_name, blank=True, verbose_name="Image 2", help_text="Index page large image")
	slug = models.SlugField(max_length=100, blank=True)
	date = models.DateField(auto_now_add=True)
	best_seller = models.BooleanField(default=False, blank=True)
	index_picture = models.BooleanField(default=False, blank=True)
	price = models.FloatField(default=4.99, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('products.views.detail', args=[str(self.id), self.slug])

	class Meta:
		ordering = ['category', 'name']


class EmailSignup(models.Model):
	email = models.EmailField(max_length=75, validators=[MaxLengthValidator(75)])

	def __unicode__(self):
		return self.email

	class Meta:
		ordering = ['email']