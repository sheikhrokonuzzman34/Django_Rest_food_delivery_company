from django.contrib import admin

from apps.restaurant.models import *
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)

