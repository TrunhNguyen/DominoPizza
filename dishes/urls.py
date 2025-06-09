from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dishes/', views.dishes_view, name='dishes'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('carting/<int:id>/', views.carting, name='carting'), 
    path('view_cart/', views.view_cart, name='view_cart'),
    path('uncarting/<int:id>/', views.uncarting, name='uncarting'),
    path('deletecart/', views.deleteall, name='deleteall'),
]