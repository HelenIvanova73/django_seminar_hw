from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, reverse
from django.views import View

from twoapp.forms import ClientForm, ProductForm
from twoapp.models import Order, Client
from datetime import timedelta
from django.utils import timezone

# Create your views here.
class GalerieView(View):
    def get(self, request):
        form = ClientForm()
        context = {
            'form': form,
            'title': 'Галерея',
        }
        return render(request, 'twoapp/index.html', context=context)

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('twoapp:galerie'))


class ListOrderView(View):
    def get(self, request):
        days = request.GET.get('days', None)
        if days is None:
            orders = Order.objects.all()
        else:
            end_date = timezone.now()
            start_date = end_date - timedelta(days=int(days))
            orders = Order.objects.filter(date_registration__range=[start_date, end_date])
        context = {
            'title': 'Список заказов',
            'orders': orders,
        }
        return render(request, 'twoapp/list_order.html', context=context)


class ProductsView(View):
    def get(self, request):
        form = ProductForm()
        context = {
            'title': 'Список продуктов',
            'form': form,
        }
        return render(request, 'twoapp/products.html', context=context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('twoapp:products'))