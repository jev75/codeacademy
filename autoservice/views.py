from django.shortcuts import render
from .models import Car, Service, Order
from django.views import generic


def index(request):
    num_cars = Car.objects.all().count()
    num_services = Service.objects.all().count()
    num_orders = Order.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_cars': num_cars,
        'num_services': num_services,
        'num_orders': num_orders,
        'num_visits': num_visits,
    }

    return render(request, 'autoservice/index.html', context=context)

class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    template_name = 'autoservice/car_list.html'


class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'autoservice/car_detail.html'

class ServiceListView(generic.ListView):
    model = Service
    template_name = 'autoservice/service_list.html'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'autoservice/service_detail.html'

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 4
    template_name = 'autoservice/order_list.html'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'autoservice/order_detail.html'

