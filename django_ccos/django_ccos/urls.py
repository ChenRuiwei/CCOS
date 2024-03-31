"""
URL configuration for django_ccos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from ccos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('canteen/', views.show_canteens),
    path('canteen/<int:canteen_id>/restaurant/', views.show_restaurants),
    path('restaurant/<int:restaurant_id>', views.show_dishes),
    path('orders', views.show_orders),
    path('order', views.order),
    path('personal/', views.personal),
    path('business/login', views.business_login),
    path('business/register', views.business_register),
    path('business/<str:business_id>/order/change/<int:indent_id>', views.change_order_state),
    path('business/<str:business_id>/order', views.business_show_orders),
    path('business/<str:business_id>/dish/<int:dish_id>/change/', views.business_change_dish),
    path('business/<str:business_id>/dish/add/', views.business_add_dish),
    path('business/<str:business_id>/dish/<int:dish_id>/delete/', views.business_delete_dish),
    path('business/<str:business_id>/dish/list/', views.business_list_dishes),
    path('business/<str:business_id>/dish', views.business_show_dishes),
    path('business/', views.business),
    path('test/', views.test),
    path('tt/', views.tt),
    path('', views.index)
]
