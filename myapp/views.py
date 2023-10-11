from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderForm
from .models import *

def home(request):
    return render(request, 'home.html', {'name': 'Oxalis'})

def add(request):
    if request.method == "POST":
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 + val2
        return render(request, 'result.html', {'result': res})
    return render(request, 'add.html')

def dashboard(request):
    ord = Order.objects.all()
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers': customers,'ord':ord})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    customers=Customer.objects.all()

    orders=customer.order_set.all()
    order_count=orders.count()

    context={'customers':customers, 'cust':customer, 'ord':orders,'ordcount':order_count}

    return render(request, 'customer.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Use reverse for redirect

    context = {'form': form}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Use reverse for redirect

    context = {'form': form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect(reverse('home'))  # Use reverse for redirect

    context = {'item': order}
    return render(request, 'delete.html', context)
