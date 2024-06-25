from django.contrib import admin
from .models import Car, Service, Order, OrderService

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'license_plate', 'VIN_code', 'year', 'brand', 'model')
    search_fields = ('client', 'license_plate', 'VIN_code', 'year', 'brand', 'model')

    class Meta:
        model = Car

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

    class Meta:
        model = Service

class OrderServiceAdmin(admin.TabularInline):
    model = OrderService
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date', 'total_sum')
    search_fields = ('car', 'date', 'total_sum')
    inlines = [OrderServiceAdmin]

    class Meta:
        model = Order

admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)