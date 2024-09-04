from django.urls import path
from .views import RestaurantCreateView, CategoryCreateView, MenuItemCreateView, OrderCreateView

urlpatterns = [
    path('restaurants/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('categories/', CategoryCreateView.as_view(), name='category-create'),
    path('menu-items/', MenuItemCreateView.as_view(), name='menu-item-create'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]