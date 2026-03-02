from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    
    # CLIENTE
    path('customers/', views.customers, name='customers'),
    path('customer/create/', views.customer_create, name='customer_create'),
]