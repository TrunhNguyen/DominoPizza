from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dishes/', views.dishes_view, name='dishes'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('carting/<int:id>/', views.carting, name='carting'), 
    path('view_cart/', views.view_cart, name='view_cart'),
    path('uncarting/<int:id>/', views.uncarting, name='uncarting'),
    path('deletecart/', views.deleteall, name='deleteall'),
    path('api/pizza/<int:id>/', views.pizza_detail, name = 'pizza_detail'),
    path('api/list/', views.pizza_list, name='pizza_list'),
    path('', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.homepage, name='homepage'),
    path('place_order/', views.place_order, name='place_order'),
    path('Admin/', views.admin_dashboard, name='admin'),
    path('orderlist/', views.order_list, name='orderlist'),
    path('orderlist/<int:order_id>/delete/', views.delete_order, name='delete_order')
]