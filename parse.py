import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drive.settings")
import django
django.setup()


from bs4 import BeautifulSoup

import re
from urllib.request import urlopen
from content.models import *


#http://radio-med.ru/makers/mrt/


# Получить HTTP страницу в виде текста
def http_request(link):
	
	return str(urlopen(link.link).read(), "utf-8")


#Наша ссылка на МРТ в магазине "Радио-мед"
link = Link.objects.all()[0]
print(link)



#Получаем страницу, расположенную по этому адресу
html = http_request(link)
# print(html)


# Список производителей
soup = BeautifulSoup(html, 'html.parser')
brands_div = soup.findAll("a", { "class" : "link_proizvod" })
brands =  [x['class'][2] for x in brands_div]


# Список строк, содержащих товары
goods_div = soup.findAll("div", { "class" : "prod_name" })
goods_str = [x.string for x in goods_div]


#Проход по производителям и по строкам
for gs in goods_str:
	for brand in brands:
		obj_b = Brand.objects.get_or_create(name = brand)[0]
		examp = re.findall(r'(?i)' + brand + ' (.+)' , gs)
		if(len(examp) != 0):
			obj_e = Examp.objects.get_or_create(name = examp[0], brand = obj_b)[0]
			obj_g = Good.objects.get_or_create(subcat = link.subcat, examp = obj_e)[0]
			print(obj_g)




