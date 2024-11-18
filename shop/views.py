from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

users = ['user1', 'user2', 'user3', 'user4', 'user5']


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, template_name='index.html', context=context)

def game(request):
    games = Game.objects.all()

    context = {
        'title': 'Игры',
        'games': games,
    }

    return render(request, template_name='games.html', context=context)

def cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, template_name='cart.html', context=context)

def sign_up_by_django(request):
    info = dict()
    if request.method == "POST":
        form = UserRegister(request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")
            age = request.POST.get("age")

            buyer = Buyer.objects.filter(name=username).first()

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif buyer:
                info['error'] = 'Пользователь уже существует'
            else:
                info['success'] = f"Приветствуем, {username}!"

            if not buyer:
                Buyer.objects.create(name=username, age=age, balance=0.00)

    else:
        form = UserRegister()

    return render(request, 'reg_page.html', {'form': form, 'info': info})


