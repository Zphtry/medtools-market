from django.db.models import *
from django.conf import settings

class Base(Model):

	name = CharField(max_length = 100, null=True, blank = True)

	def __str__(self): return self.name

	def natural_key(self): return self.name

	class Meta: abstract = True

class Domain(Base): img = CharField(max_length=200, null=True, blank=True)


class Supcat(Base): domain = ForeignKey(Domain, related_name = "supcat")

class Cat(Base):

	supcat = ForeignKey(Supcat, related_name = "cat")

	img = CharField(max_length=200, null=True, blank=True)

class Subcat(Base): cat = ForeignKey(Cat, related_name="subcat")

class Prop(Base):

	subcat = ManyToManyField(Subcat, related_name="props")
	


class Value(Base):  prop = ForeignKey(Prop, related_name="values")

class PropValue(Model):

	prop = ForeignKey(Prop, null=True, blank=True)

	value = ForeignKey(Value, null=True, blank=True)

	def __str__(self): return str(self.prop) + ' ' + str(self.value)




