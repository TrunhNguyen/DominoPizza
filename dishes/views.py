from django.http import HttpResponse
from django.template import loader
from .models import Products, Orders
from django.shortcuts import redirect, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PizzaSerializers
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def dishes_view(request):
    pizzalist = Products.objects.all().values()
    template = loader.get_template('pizzalist.html')
    context = {
        'pizzalist': pizzalist,
    }
    return HttpResponse(template.render(context, request))

@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def comingsoon(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())

@login_required
def carting(request, id):
    cart = request.session.get('cart', {})
    dish = get_object_or_404(Products, id=id)
    item_id = str(dish.id)
    if item_id in cart:
        cart[item_id]['quantity'] += 1
    else:
        cart[item_id] = {
            'name': dish.name,
            'price': int(float(dish.price)),
            'quantity': 1
        }
    request.session['cart'] = cart
    return redirect(view_cart)

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {
        'cart': cart,
        'total_price': int(total_price),
    }
    return render(request, 'cart.html', context)

@login_required
def uncarting(request, id):
    cart = request.session.get('cart', {})
    dish = get_object_or_404(Products, id=id)
    item_id = str(dish.id)

    if item_id in cart:
        cart[item_id]['quantity'] -= 1
        if cart[item_id]['quantity'] == 0:
            del cart[item_id]
    request.session['cart'] = cart
    return redirect(view_cart)

@login_required
def deleteall(request):
    request.session['cart'] = {}
    return redirect(view_cart)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_raw = request.POST['password']
        password2 = request.POST['password2']
        if not username or not password_raw:
            messages.error(request, 'Tên đăng nhập và mật khẩu không được để trống.')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tên đăng nhập đã tồn tại.')
            return render(request, 'register.html')
        if password_raw != password2:
            messages.error(request, 'Hai mật khẩu không khớp')
            return render(request, 'register.html')
        user = User.objects.create_user(username=username, password=password_raw)
        user.save()
        return redirect('login')
    return render(request, 'register.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('homepage')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
            return render(request, 'login.html')
    return render(request, 'login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def place_order(request):
    cart = request.session.get('cart', {})
    for product_id, item in cart.items():
        try:
            product = Products.objects.get(id=product_id)
            Orders.objects.create(
                product=product,
                customer=request.user,
                quantity=item['quantity']
            )
        except Products.DoesNotExist:
            pass
    request.session['cart'] = {}  
    return render(request, 'order_alert.html')

def admin_dashboard(request):
    return render(request, 'admin.html')

def order_list(request, id):
    dish = get_object_or_404(Products, id=id)


@api_view(['GET'])
def pizza_detail(request, id):
    try:
        pizza = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response({'error': 'Pizza not found'}, status=404)
    serializer = PizzaSerializers(pizza)
    return Response(serializer.data)


@api_view(['GET'])
def pizza_list(request):
    pizza = Products.objects.all()
    serializer = PizzaSerializers(pizza, many=True)
    return Response(serializer.data)

