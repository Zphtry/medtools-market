from django.contrib import admin
import django.apps


for x in django.apps.apps.get_models():
	if 'content.' in str(x): admin.site.register(x)


    

