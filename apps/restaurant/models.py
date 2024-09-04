from django.db import models
from django.contrib.auth import get_user_model

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_restaurants')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

class Order(models.Model):
    PENDING = 'pending'
    PAID = 'paid'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
    ]

    customer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    payment_method = models.CharField(max_length=10, choices=[('card', 'Card'), ('cash', 'Cash')])

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in Order #{self.order.id}"
