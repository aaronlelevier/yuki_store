import datetime

from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from products.models import Product, Category, Color, EmailSignup, Style


def create_category():
	return Category.objects.create(name='Hats')

def create_color():
	return Color.objects.create(name='red')

def create_style():
	return Style.objects.create(name='baby')

def create_product(name):
	create_category()
	create_color()
	create_style()
	return Product.objects.create(name=name, 
								category_id=1, 
								description="nice hat", 
								picture="hat.jpg",
								best_seller=True,
								index_picture=True
								)

class ProductMethodTests(TestCase):

	def test_date_and_slug_is_not_null(self):
		"""
		tests that date_auto_now_add is working correctly
		"""
		new_product = create_product(name='index_blank_test')
		date_test = new_product.date == datetime.date.today()
		self.assertEqual(date_test, True)

		if new_product.slug == None: 
			slug_test = False
		else:
			slug_test = True
		self.assertEqual(slug_test, True)

class ViewTests(TestCase):

	def test_index_view(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_admin_view(self):
		response = self.client.get('/admin/')
		self.assertEqual(response.status_code, 200)

class IndexViewTests(TestCase):

	def test_index_view_using_reverse(self):
		"""
		test blank Index page
		"""
		response = self.client.get(reverse('products:index'))
		self.assertEqual(response.status_code, 200)

		all_context = ['main_slider','latest_products', 'best_seller', 'ad_banner',
						'categories', 'popular_styles']
		for i in all_context:
			self.assertQuerysetEqual(response.context[i], [])

	def test_products_with_content(self):
		"""
		tests the index page with DB test_with_content
		"""
		create_product(name='index_test')

		response = self.client.get(reverse('products:index'))

		all_context = ['main_slider', 'latest_products', 'best_seller', 'ad_banner']
		for i in all_context:
			self.assertQuerysetEqual(
				response.context[i],
				['<Product: index_test>']
				)

	def test_categories(self):
		"""
		test categories queryset
		"""
		create_category()
		response = self.client.get(reverse('products:index'))
		self.assertQuerysetEqual(
			response.context['categories'],
			['<Category: Hats>']
			)

	def test_styles(self):
		"""
		test styles queryset
		"""
		create_style()
		response = self.client.get(reverse('products:index'))
		self.assertQuerysetEqual(
			response.context['popular_styles'],
			['<Style: baby>']
			)
