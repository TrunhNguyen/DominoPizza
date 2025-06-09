# dishes/views.py
from django.http import HttpResponse
from django.template import loader
from .models import Pizza
from django.shortcuts import redirect, get_object_or_404, render

def dishes_view(request):
  pizzalist = Pizza.objects.all().values()
  template = loader.get_template('pizzalist.html')
  context = {
    'pizzalist': pizzalist,
  }
  return HttpResponse(template.render(context, request))

def homepage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def comingsoon(request):
  template = loader.get_template('404.html')
  return HttpResponse(template.render())

def carting(request, id):
  cart = request.session.get('cart', {})
  dish = get_object_or_404(Pizza, id=id)
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

def view_cart(request):
  cart = request.session.get('cart', {})
  total_price = sum(item['price'] * item['quantity'] for item in cart.values())
  context = {
    'cart': cart,
    'total_price': int(total_price),
  }
  return render(request, 'cart.html', context)

def uncarting(request, id):
  cart = request.session.get('cart', {})
  dish = get_object_or_404(Pizza, id=id)
  item_id = str(dish.id)

  if item_id in cart:
    cart[item_id]['quantity'] -= 1
    if cart[item_id]['quantity'] == 0:
      del cart[item_id]
  request.session['cart'] = cart
  return redirect(view_cart)

def deleteall(request):
  cart = request.session.get('cart', {})
  request.session['cart'] = {}
  return redirect(view_cart)