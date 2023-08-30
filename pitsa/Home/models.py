from django.db import models
import uuid


class PizzaSize(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class PizzaCrust(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class PizzaSauce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class PizzaTopping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE,default='Small')
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE,default='Regular')
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE,default='Tomato')
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE,default='Mozzarella')
    selected_topping = models.ForeignKey(PizzaTopping, on_delete=models.CASCADE, related_name='selected_topping_orders')
    additional_toppings = models.ManyToManyField(PizzaTopping, blank=True, related_name='additional_topping_orders')
    quantity = models.IntegerField(default='1')
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=10, default='')
    delivery_address = models.TextField(default='')
    door_no = models.CharField(max_length=10,default='')
    county = models.CharField(max_length=10,default='')
    country = models.CharField(max_length=10,default='Ireland')
    eircode = models.CharField(max_length=10,default='')
    street = models.CharField(max_length=20,default='')


    total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.order_id} - {self.name}"


class Payment(models.Model):
    card_number = models.CharField(max_length=16,default='')
    expiry_date = models.CharField(max_length=10,default='')
    cvv = models.CharField(max_length=3,default='')
    card_name = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=200,default='')
    phone_number = models.CharField(max_length=20,default='')
    email = models.EmailField(default='')
