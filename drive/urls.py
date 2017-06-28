from django.conf.urls import url, include
from django.contrib   import admin
from content.views import *


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', MainPage.as_view(), name = 'main'),
	url(r'^dom_(\d+)$', DomainPage.as_view(), name = 'domain'),
	url(r'^cat_(\d+)$', SearchPage.as_view(), name = 'search'),
	url(r'^prod_(?P<pk>\d+)$', ProdPage.as_view(), name = 'prod'),
]
