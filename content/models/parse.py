from django.db.models import *
from .goods import *
from .cats_props import *

class Link(Model):
    
    shop = ForeignKey(Shop, null=True, blank=True)
    
    subcat = ForeignKey(Subcat, null=True, blank=True)

    link = CharField(max_length=300, null=True, blank=True)

    def __str__(self): return str(self.shop) + ' ' + str(self.subcat)