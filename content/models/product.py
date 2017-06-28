from django.db.models import *
from django.conf import settings
from .struct import *


class Brand(Base): pass

class ModelPrd(Base):
	brand = ForeignKey(Brand, related_name="modelprds", null=True, blank=True)


class Shop(Base): pass

class Price(Model):

	price = PositiveIntegerField()

	shop  = ForeignKey(Shop, null=True, blank=True)

	def __str__(self):
		s = str(round(self.price,-len(str(self.price)) + 2))
		if 3 < len(s) <= 6: return s[:-3] + ' ' + s[-3:]
		if 6 < len(s): return s[:-6] + ' ' + s[-6:-3] + ' ' + s[-3:]


class Prod(Model):

	subcat = ForeignKey(Subcat, null=True, blank=True)

	modelprd = ForeignKey(ModelPrd, related_name="prods", null=True, blank=True)

	price = ManyToManyField(Price, blank=True)

	img = CharField(max_length=200, null=True, blank=True)

	propvalue = ManyToManyField(PropValue)

	def __str__(self): return str(self.modelprd.brand) + ' ' + str(self.modelprd)