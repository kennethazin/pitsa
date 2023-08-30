from django import forms
from django.forms import ModelForm
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['size', 'crust', 'sauce', 'cheese', 'selected_topping', 'additional_toppings', 'quantity', 'name', 'email', 'phone_number', 'street', 'eircode', 'country', 'county', 'door_no' ]
        
    additional_toppings = forms.ModelMultipleChoiceField(queryset=PizzaTopping.objects.all(), widget=forms.CheckboxSelectMultiple)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'expiry_date', 'cvv', 'card_name', 'name', 'address', 'phone_number', 'email']
