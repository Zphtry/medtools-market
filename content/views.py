from django.views.generic import *
from .models import *
from django.core import serializers
from django.utils.encoding import *
import json


def utf16totext(txt):
	for i, x in enumerate(txt):
		if txt[i:i + 2] == chr(92) + 'u':
			txt = txt.replace(txt[i:i + 6], chr(int(txt[i + 2:i + 6], 16)))
	return txt

class MainPage(ListView):

	template_name = '1_main_page.html'

	context_object_name = 'Domain'

	def get_queryset(self): return Domain.objects.all()

class DomainPage(ListView):

	template_name = '2_domain_page.html'
	context_object_name = 'obj'

	def get_queryset(self):
		
		context = {
			'domain':Domain.objects.get(id = self.args[0])
		}
		return context

class SearchPage(ListView):

	template_name = '3_search_page.html'

	context_object_name = 'obj'

	def get_queryset(self):

		data = serializers.serialize("json", Prod.objects.all(), use_natural_foreign_keys = True)

		print(utf16totext(data))

		cat     = Cat.objects.get(id = self.args[0])
		subcats = Subcat.objects.filter(cat = cat)

		comm = Prop.objects.filter(subcat = subcats[0])

		for subcat in subcats[1:]:
			comm = comm & Prop.objects.filter(subcat = subcat)

		prods = Prod.objects.filter(subcat__in = subcats)

		brands = set()

		for prod in prods: brands.add(prod.modelprd.brand)

		context = {
			'domain': cat.supcat.domain,
			'cat':cat,
			'subcats':subcats,
			'comm':comm,
			'prods':prods,
			'brands': brands,
		}

		return context

	# def get(self, request, *args, **kwargs):
	# 	print('abc')
	# 	view = AuthorDisplay.as_view()
	# 	return view(request, *args, **kwargs)

class ProdPage(DetailView):

	template_name = '4_prod_page.html'
	model = Prod


# class SearchPage(ListView):

#     template_name = '2_search_page.html'

#     context_object_name = 'obj'


#     def get_queryset(self):

		
#         cat     = Cat.objects.get(id = self.args[0])
#         subcats = Subcat.objects.filter(cat = cat)

#         comm = Prop.objects.filter(subcat = subcats[0])
		
#         for subcat in subcats[1:]:
#             comm = comm & Prop.objects.filter(subcat = subcat)

#         goods = Good.objects.filter(subcat__in = subcats)

#         brands = set()

#         for good in goods: brands.add(good.examp.brand)

#         print(brands)

#         context = {
#             'cat':cat,
#             'subcats':subcats,
#             'comm':comm,
#             'goods': goods,
#             'brands': brands
#         }

#         return context
		# goods   = Good.objects.filter(cat = cat)
		# com_props = Prop.objects.filter(subcat = subcats[0])

	#     context = {
	#         'cat':cat,
	#         'subcats':subcats,
	#         'goods':goods,
	#         'com_props':com_props,
	#     }

	#     return context


		
