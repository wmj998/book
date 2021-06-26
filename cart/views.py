from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.shortcuts import render, redirect

# Create your views here.
from cart.models import Cart
from manager.models import Book
from order.models import Order


@login_required
def index(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    money = 0
    numbers = len(carts)
    for cart in carts:
        money += cart.all_price
    page_num = request.GET.get('page', 1)
    paginator = Paginator(carts, 4)
    page_now = paginator.page(page_num)
    return render(request, 'cart.html', locals())


@login_required
def checkout(request):
    username = request.user
    books = Cart.objects.filter(user=username)
    for commodity in books:
        Order.objects.create(all_price=commodity.all_price, user=username)
    books.delete()
    return render(request, 'checkout.html', locals())


@login_required
def add_cart(request):
    page = request.GET.get('page')
    user = request.user
    id = request.GET.get('id')
    book = Book.objects.get(id=id)
    commoditys = Cart.objects.filter(Q(book_name=book.book_name) & Q(user=user))
    if commoditys:
        commodity = Cart.objects.get(book_name=book.book_name)
        commodity.number = F('number') + 1
        commodity.all_price = F('all_price') + commodity.one_price
        commodity.save()
        return redirect(f'/user/index/?page={page}')
    Cart.objects.create(book_name=book.book_name, number=1, one_price=book.book_price,
                        all_price=book.book_price, user=user)
    return redirect(f'/user/index/?page={page}')


@login_required
def delete_cart(request):
    id = request.GET.get('id')
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('/cart/index/')


@login_required
def delete_all(request):
    user = request.user
    cart = Cart.objects.filter(user_id=user.id)
    if cart:
        cart.delete()
    return redirect('/cart/index/')
