from django.contrib import admin
from .models import MenuItem, Category, OrderModel,CanteenList, Availability

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(CanteenList)
admin.site.register(Availability)