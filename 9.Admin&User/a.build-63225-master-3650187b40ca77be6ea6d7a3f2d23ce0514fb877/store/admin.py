from django.contrib import admin

from .models import Product, Address, Company, Category


# Example
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter = ['category', 'company']
    sortable_by = ['price']
    list_display_links = ['id', 'name']


# Add the rest of admin models here
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_address', 'city']
    list_filter = ['city']


class ProductTabular(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProductTabular]


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]