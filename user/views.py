from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from manager.models import Book
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repwd = request.POST['repwd']
        email = request.POST['email']
        user = User.objects.filter(username=username)
        if user:
            error = '该用户已注册'
            return render(request, 'regist.html', locals())
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('/user/register_success/')
        except Exception as e:
            print('--- user register error %s' % (e))
            return render(request, 'regist.html', locals())


@login_required
def register_success(request):
    username = request.user
    return render(request, 'regist_success.html', locals())


def login_user(request):
    if request.method == 'GET':
        global next
        next = request.GET.get('next')
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username:
            error = '请输入用户名'
            return render(request, 'login.html', locals())
        if not password:
            error = '请输入密码'
            return render(request, 'login.html', locals())
        user = authenticate(username=username, password=password)
        if not user:
            error = '用户名或密码错误'
            return render(request, 'login.html', locals())
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/user/login_success/')


@login_required
def login_success(request):
    username = request.user
    return render(request, 'login_success.html', locals())


def logout_user(request):
    logout(request)
    return redirect('/index/')


@login_required
def index(request):
    username = request.user
    books = Book.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(books, 4)
    page_now = paginator.page(page_num)
    number_all = len(books)
    return render(request, 'user_index.html', locals())


@login_required
def delete_user(request):
    username = request.user
    if request.method == 'GET':
        return render(request, 'delete.html', locals())
    elif request.method == 'POST':
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            error = '您输入的密码有误'
            return render(request, 'delete.html', locals())
        user.delete()
        return redirect('/index/')


@login_required
def exchange(request):
    pn = request.POST['pn']
    return redirect(f'/user/index/?page={pn}')


@login_required
def query(request):
    username = request.user
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
    return render(request, 'query.html', locals())


@login_required
def exchange_query(request):
    min = request.GET.get('min')
    max = request.GET.get('max')
    pn = request.POST['pn']
    return redirect(f'/user/query/?page={pn}&min={min}&max={max}')
