from django.db import models


class Account(models.Model):
    email = models.EmailField(unique=True)
    image = models.ImageField(
        upload_to='storage/account', null=True, blank=True)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=64)
    dateOfBirth = models.DateField(verbose_name='Date Of Birth')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} : {self.email}'


class Seller(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name='seller')
    paymentID = models.CharField(max_length=12, verbose_name='Payment ID')
    billing = models.TextField(max_length=256, verbose_name='Billing Address')
    revenue = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} : {self.account.name}'


class Customer(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name='customer')
    credit = models.PositiveIntegerField(
        default=0, verbose_name='Store Credit')

    def __str__(self):
        return f'{self.account.id} : {self.account.name}'


class Product(models.Model):
    PRODUCT_CATAGORY = [('EARP', 'Earphones'), ('HEAD', 'Headphones'),
                        ('LAPT', 'Laptops'), ('VIRT', 'VR Headsets')]
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='storage/product', null=True, blank=True)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=4096)
    specifications = models.TextField(max_length=4096)
    mrp = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(
        max_length=4, choices=PRODUCT_CATAGORY, db_index=True)
    inStock = models.BooleanField(default=True, verbose_name='In Stock')
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.category}-{self.id} : {self.name}'


class CartItem(models.Model):
    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.customer}, {self.product}'


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    locality = models.TextField(max_length=256)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.customer}, {self.locality}'


class Review(models.Model):
    PRODUCT_RATING = [(10, 'One'), (20, 'Two'),
                      (30, 'Three'), (40, 'Four'), (50, 'Five')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=PRODUCT_RATING)
    message = models.TextField(max_length=512, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} : {self.message[:50]}'


class Order(models.Model):
    ORDER_STATUS = [('PEN', 'Pending'), ('DEL', 'Delivered'),
                    ('CNL', 'Cancelled')]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default='PEN', db_index=True)

    def __str__(self):
        return f'{self.customer} : {self.product}'
