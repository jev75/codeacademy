from django.urls import path
from . import views

app_name = 'autoservice'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.CarListView.as_view(), name='cars'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    ]