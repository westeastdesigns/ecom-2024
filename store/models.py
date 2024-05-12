import datetime

from django.db import models


class Category(models.Model):
    """Category defines the database tables for categories of Products.

    Args:
        name (CharField): name for the category of product

    Returns:
        CharField: the name of the category
    """

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Customer defines the database tables populating basic info about customers

    Args:
        first_name (CharField): customer's first name
        last_name (CharField): customer's last name
        phone (CharField): customer's phone number
        email (EmailField): customer's email address
        password (CharField): customer's password, type will be updated for security

    Returns:
        CharField: customer's first and last name
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    """Product defines database tables for all products

    Args:
        name (CharField): name of product
        price (DecimalField): price of product
        category (ForeignKey): references Category table for name of product category
        description (TextField): description of product
        image (ImageField): image of product
        is_sale (BooleanField): is it on sale or not, false by default
        sale_price (DecimalField): price of product while on sale

    Returns:
        CharField: name of product
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=1500, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/product/")

    # support for sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order defines database tables for customer orders.

    Args:
        product (ForeignKey): references the Product table
        customer (ForeignKey): references the Customer table
        quantity (IntegerField): number of product ordered
        address (CharField): customer's address
        phone (CharField): customer's phone number
        date (DateField): when customer placed the order
        status (BooleanField): status of order, shipped or not

    Returns:
        ForeignKey: returns name of product
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
