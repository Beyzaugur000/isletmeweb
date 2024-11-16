from django.db import models # type: ignore
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_description = models.CharField(max_length=100)

    def __str__(self):
        return self.region_description

    class Meta:
        db_table = 'region'
        managed = False

class Territories(models.Model):
    territory_id = models.AutoField(primary_key=True)
    territory_description = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='territories')

    def __str__(self):
        return self.territory_description

    class Meta:
        db_table = 'territories'
        managed = False

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    title_of_courtesy = models.CharField(max_length=25)
    birth_date = models.DateField()
    hire_date = models.DateField()
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=15)
    region = models.CharField(max_length=15, null=True, blank=True)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    home_phone = models.CharField(max_length=24)
    extension = models.CharField(max_length=4)
    photo = models.BinaryField(null=True, blank=True)
    notes = models.TextField()
    reports_to = models.IntegerField(null=True, blank=True)
    photo_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'employees'
        managed = False


class EmployeeTerritories(models.Model):
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE, primary_key=True)
    territory = models.ForeignKey(Territories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee_territories'
        managed = False

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='categories_pictures/', blank=True, null=True)
 

    class Meta:
        db_table = 'categories'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.category_name
  

class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'suppliers'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.company_name

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    quantity_per_unit = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    units_in_stock = models.IntegerField(blank=True, null=True)
    units_on_order = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(blank=True, null=True)
    discontinued = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.product_name


class UsStates(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    state_abbr = models.CharField(max_length=2)
    state_region = models.CharField(max_length=255)

    class Meta:
        db_table = 'us_states'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.state_name


class Shippers(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, null=True, blank=True)

    class Meta :
    
        db_table = 'shippers'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.company_name


class Customers(models.Model):
    customer_id = models.CharField(max_length=5, primary_key=True)
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_title = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'customers'
        managed = False  # Bu tablo Django tarafından yönetilmeyecek (var olan bir tablo)

    def __str__(self):
        return self.company_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE, related_name='orders')
    employee_id = models.IntegerField(null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    required_date = models.DateTimeField(null=True, blank=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    ship_via = models.IntegerField(null=True, blank=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ship_name = models.CharField(max_length=255, null=True, blank=True)
    ship_address = models.CharField(max_length=255, null=True, blank=True)
    ship_city = models.CharField(max_length=100, null=True, blank=True)
    ship_region = models.CharField(max_length=100, null=True, blank=True)
    ship_postal_code = models.CharField(max_length=20, null=True, blank=True)
    ship_country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'orders'
        managed = False 

    def __str__(self):
        return f"Order {self.order_id} - {self.customer.company_name}"

class OrderDetails(models.Model):
    order = models.OneToOneField(Orders, on_delete=models.CASCADE,primary_key=True)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='order_details')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.FloatField()

    class Meta:
        db_table = 'order_details'
        managed = False 

    def __str__(self):
        return f"Order {self.order.order_id} - Product {self.product.product_id}"
    
    from django.db import models # type: ignore

class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(max_length=10, primary_key=True)
    customer_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.customer_type_id

    class Meta:
        db_table = 'customer_demographics'
        managed= False

class CustomerCustomerDemo(models.Model):
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE,primary_key=True)
    customer_type = models.ForeignKey(CustomerDemographics, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} - {self.customer_type}"

    class Meta:
        db_table = 'customer_customer_demo'
        unique_together = ('customer', 'customer_type')
        managed=False