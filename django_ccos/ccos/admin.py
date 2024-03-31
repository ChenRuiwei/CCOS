from django.contrib import admin

from ccos.models import *

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Indent)
admin.site.register(IndentDish)

admin.site.register(Customer)
admin.site.register(Canteen)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Business)
admin.site.register(Administrator)
admin.site.register(Category)
