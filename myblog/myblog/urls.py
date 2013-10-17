from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

	url(r'', include('products.urls', namespace='products')),
	
    # url(r'^checkout/', include('paypal_express_checkout.urls')),
)
