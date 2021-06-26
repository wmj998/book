from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from manager.models import Book
from order.models import Order


@login_required
def index(request):
    return render(request, 'manager.html')


@login_required
def book_manager(request):
    books = Book.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(books, 5)
    page_now = paginator.page(page_num)
    return render(request, 'book_manager.html', locals())


@login_required
def add_book(request):
    if request.method == 'GET':
        return render(request, 'book_add.html')
    elif request.method == 'POST':
        name = request.POST['book_name']
        price = request.POST['book_price']
        author = request.POST['book_author']
        sales = request.POST['book_sales']
        stock = request.POST['book_stock']
        Book.objects.create(book_name=name, book_price=price, book_author=author,
                            book_sales=sales, book_stock=stock)
        return redirect('/manager/book_manager/')


@login_required
def update_book(request):
    id = request.GET.get('id')
    book = Book.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'book_edit.html', locals())
    elif request.method == 'POST':
        name = request.POST['book_name']
        price = request.POST['book_price']
        author = request.POST['book_author']
        sales = request.POST['book_sales']
        stock = request.POST['book_stock']
        book.book_name = name
        book.book_price = price
        book.book_author = author
        book.book_sales = sales
        book.book_stock = stock
        book.save()
        return redirect('/manager/book_manager/')


@login_required
def delete_book(request):
    id = request.GET.get('id')
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/manager/book_manager/')


@login_required
def order(request):
    orders = Order.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(orders, 4)
    page_now = paginator.page(page_num)
    return render(request, 'order_manager.html', locals())


@login_required
def state(request):
    id = request.GET.get('id')
    page = request.GET.get('page')
    order = Order.objects.get(id=id)
    order.state = '已发货'
    order.save()
    return redirect(f'/manager/order/?page={page}')
