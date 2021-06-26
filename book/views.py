from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from manager.models import Book


def index(request):
    books = Book.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(books, 4)
    page_now = paginator.page(page_num)
    number_all = len(books)
    return render(request, 'index.html', locals())


def exchange(request):
    pn = request.POST['pn']
    return redirect(f'/index/?page={pn}')


def query(request):
    if request.method == 'POST':
        min = request.POST['min']
        max = request.POST['max']
    elif request.method == 'GET':
        min = request.GET.get('min', 0)
        max = request.GET.get('max', 0)
    books = Book.objects.filter(Q(book_price__gte=min) & Q(book_price__lte=max))
    page_num = request.GET.get('page', 1)
    paginator = Paginator(books, 4)
    page_now = paginator.page(page_num)
    number_all = len(books)
    return render(request, 'query_index.html', locals())


def exchange_query(request):
    min = request.GET.get('min')
    max = request.GET.get('max')
    pn = request.POST['pn']
    return redirect(f'/query/?page={pn}&min={min}&max={max}')
