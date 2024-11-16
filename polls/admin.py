from django.contrib import admin # type: ignore
from .models import MyModel
class MyModelAdmin(admin.ModelAdmin):
    # Define the fields you want to display in the list view
    list_display = ('field1', 'field2', 'field3')

    # Define the fields you want to filter in the list view
    list_filter = ('field1', 'field2')

    # Define the fields you want to search in the list view
    search_fields = ('field1', 'field2')


admin.site.site_header = "İşletme Takip Yönetici Paneli"
admin.site.site_title = "İşletme Yönetimi"
admin.site.index_title = "Hoş Geldiniz İşletme Yönetim Paneline"




from .models import Region, Territories, Employees, EmployeeTerritories,Categories, Suppliers,Products,UsStates,Shippers, Customers,Orders,OrderDetails, CustomerDemographics, CustomerCustomerDemo

# Region admin configuration
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_description')

admin.site.register(Region, RegionAdmin)

# Territories admin configuration
class TerritoriesAdmin(admin.ModelAdmin):
    list_display = ('territory_id', 'territory_description', 'region')

admin.site.register(Territories, TerritoriesAdmin)

# Employees admin configuration
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'title', 'hire_date', 'country')

 
    list_filter = ('country', 'hire_date')

admin.site.register(Employees, EmployeesAdmin)

class EmployeeTerritoriesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'territory_id')

admin.site.register(EmployeeTerritories, EmployeeTerritoriesAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'description')
  

admin.site.register(Categories, CategoriesAdmin)

class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'company_name', 'contact_name', 'country', 'phone')


admin.site.register(Suppliers, SuppliersAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'supplier', 'category', 'unit_price', 'units_in_stock', 'discontinued')

    list_filter = ('supplier', 'category', 'discontinued')

admin.site.register(Products, ProductsAdmin)



class UsStatesAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name', 'state_abbr', 'state_region')
  
    list_filter = ('state_region',)

admin.site.register(UsStates, UsStatesAdmin)



class ShippersAdmin(admin.ModelAdmin):
    list_display = ('shipper_id', 'company_name', 'phone')

admin.site.register(Shippers,ShippersAdmin)




class CustomersAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'contact_title', 'city', 'country', 'phone')
    list_filter = ('country', 'city')
admin.site.register(Customers,CustomersAdmin)



class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date', 'required_date', 'shipped_date', 'ship_via', 'freight')
    list_filter = ('order_date', 'required_date', 'shipped_date', 'ship_country')
admin.site.register(Orders,OrdersAdmin)




class OrderDetailsAdmin(admin.ModelAdmin):
   list_display = ('order', 'product', 'unit_price', 'quantity', 'discount')
   search_fields = ('order__order_id', 'product__product_id', 'product__product_name')
   list_filter = ('order__order_id', 'product__product_name') 


admin.site.register(OrderDetails,OrderDetailsAdmin)



class CustomerDemographicsAdmin(admin.ModelAdmin):
    list_display = ('customer_type_id', 'customer_desc')
    search_fields = ('customer_type_id', 'customer_desc')
admin.site.register(CustomerDemographics,CustomerDemographicsAdmin)

class CustomerCustomerDemoAdmin(admin.ModelAdmin):
    list_display = ('customer', 'customer_type')
    search_fields = ('customer__company_name', 'customer_type__customer_type_id')
    list_filter = ('customer__country',)
admin.site.register(CustomerCustomerDemo,CustomerCustomerDemoAdmin) 