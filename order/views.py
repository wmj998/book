from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from order.models import Order


@login_required
def index(request):
    username = request.user
    orders = Order.objects.filter(user=username)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(orders, 4)
    page_now = paginator.page(page_num)
    return render(request, 'order.html', locals())


@login_required
def state(request):
    id = request.GET.get('id')
    page = request.GET.get('page')
    order = Order.objects.get(id=id)
    order.state = '已收货'
    order.save()
    return redirect(f'/order/index/?page={page}')
