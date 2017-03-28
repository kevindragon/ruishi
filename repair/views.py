from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderStatus
from django.db import models


# Create your views here.
def index(request):
    number = request.GET.get('number', '')
    context = {'number': number}
    if number is not '':
        try:
            order = Order.objects.get(number=number)
            if order is not None:
                context['order'] = order
                context['status'] = order.orderstatus_set.all().order_by('-created_at')
        except models.ObjectDoesNotExist:
            pass
    return render(request, 'repair/index.html', context)

