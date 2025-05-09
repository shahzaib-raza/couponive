from django.contrib import admin
from .models import Store, Coupon

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'store', 'is_active', 'created_at')
    list_filter = ('store', 'is_active')
    search_fields = ('title', 'code', 'description')