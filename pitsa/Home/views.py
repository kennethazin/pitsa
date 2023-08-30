from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm, PaymentForm
from .models import *
import datetime
import uuid # to generate unique order id
from django.http import JsonResponse



def home(request):
    return render(request, 'index.html')


def menu(request):
    total_price = 0  # Initialize total_price to 0
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Get form data
            size_id = form.cleaned_data.get('size').id
            crust_id = form.cleaned_data.get('crust').id
            sauce_id = form.cleaned_data.get('sauce').id
            cheese_id = form.cleaned_data.get('cheese').id

            selected_topping_id = form.cleaned_data.get('selected_topping').id
            additional_toppings_ids = [topping.id for topping in form.cleaned_data.get('additional_toppings')]
            quantity = form.cleaned_data.get('quantity')

            # Get prices of all selected items
            size_price = PizzaSize.objects.get(id=size_id).price
            crust_price = PizzaCrust.objects.get(id=crust_id).price
            sauce_price = PizzaSauce.objects.get(id=sauce_id).price
            cheese_price = Cheese.objects.get(id=cheese_id).price
            selected_topping_price = PizzaTopping.objects.get(id=selected_topping_id).price
            additional_topping_prices = [topping.price for topping in PizzaTopping.objects.filter(id__in=additional_toppings_ids)]

            # Calculate total price
            def calculatePrice(size_price, crust_price, sauce_price, cheese_price, selected_topping_price, additional_topping_prices, quantity):
                base_price = size_price + crust_price + sauce_price + cheese_price + selected_topping_price
                additional_toppings_prices = sum(additional_topping_prices)
                return (base_price + additional_toppings_prices) * quantity
            
            total_price = calculatePrice(size_price, crust_price, sauce_price, cheese_price, selected_topping_price, additional_topping_prices, quantity)

            # Create order object
            order = form.save(commit=False)
            order.size_id=size_id
            order.crust_id=crust_id
            order.sauce_id=sauce_id
            order.cheese_id=cheese_id
            order.selected_topping_id=selected_topping_id
            order.quantity=quantity
            order.total_price=total_price

            # Generate and set order ID
            order_id = uuid.uuid4().hex
            order.order_id = order_id

            # Save order object
            order.save()
            order.additional_toppings.set(additional_toppings_ids)
            order.save()

            # Store order ID in session
            request.session['order_id'] = order_id
            request.session['total_price'] = str(total_price)

            # Redirect to confirmation page
            return redirect('payment')
    else:
        form = OrderForm()
        total_price = 0  # Add this line to initialize total_price

    return render(request, 'menu.html', {'form': form, 'total_price': total_price})

def payment(request):
    order_id = request.session.get('order_id')
    if not order_id:
        messages.error(request, 'Invalid request. Please place an order first.')
        return redirect('menu')

    order = Order.objects.get(order_id=order_id)
    current_time = datetime.datetime.now()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the payment here using the form data
            # ...

            # Clear the order ID and total price from the session
            del request.session['order_id']
            del request.session['total_price']

            # Redirect to the confirmation page
            return redirect('confirmation')
        else:
            # messages.error(request, 'Invalid payment information. Please try again.')
            return redirect('confirmation')

    else:
        form = PaymentForm()
 # just to show what would happen if it were properly implemented


    context = {
        'current_time': current_time,
        'crust': order.crust,
        'cheese': order.cheese,
        'size': order.size,
        'selected_topping': order.selected_topping,
        'additional_toppings': order.additional_toppings.all(),
        'total_price': order.total_price,
        'order_id': order_id,
        'form': form,
    }

    return render(request, 'payment.html', context)

def confirmation(request):
    current_time = datetime.datetime.now()
    order_id = request.session.get('order_id')
    selected_topping_id = request.session.get('selected_topping')
    if not order_id:
        messages.error(request, 'Invalid request. Please place an order first.')
        return redirect('confirmation')
    order = Order.objects.get(order_id=order_id)
    total_price = request.session.get('total_price')
    if not total_price:
        messages.error(request, 'Invalid request. Total price not found.')
        return redirect('confirmation')
    del request.session['total_price']
    del request.session['order_id']
    context = {
        'order': order,
        'total_price': total_price,
        'current_time': current_time,
        'order_id': order_id,
       'selected_topping_id': selected_topping_id,
    }
    return render(request, 'confirmation.html', context)
