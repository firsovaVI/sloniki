from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse

import sys
sys.path.append('../elephant')
from authentication.models import User

from .models import Problem


def index(request):
    """Функция отображения главной страницы сайта"""
    is_auth = True

    # Проверить, есть ли у пользователя идентификатор сессии
    try:
        id = request.session["session_id"]
    except KeyError:
        is_auth = False

    # Взять список проблем из базы данных
    problems_list = Problem.objects.all()

    # Взять HTML-шаблон главной страницы
    template = loader.get_template("index.html")

    # Определить контент шаблона
    contex = {"problems_list": problems_list, "is_auth": is_auth}

    # Сделать рендер веб-страницы и отправить ответ
    return HttpResponse(template.render(contex, request))


def detail(request, problem_id):
    """Функция отображения детальной информации по задаче"""
    is_auth = True

    # Проверить, есть ли у пользователя идентификатор сессии
    try:
        id = request.session["session_id"]
    except KeyError:
        is_auth = False

    # Получить задачу по первичному ключу из базы данных
    p = Problem.objects.get(pk=problem_id)
    if p.image:
        problem = {"headline": p.headline, "image_url": p.image.url, "statement": p.statement, "answer": p.answer}
    else:
        problem = {"headline": p.headline, "image_url": None, "statement": p.statement, "answer": p.answer}

    # Взять необходимый HTML-шаблон
    template = loader.get_template("detail.html")

    # Определить задачу и правильность ответа в контексте
    contex = {"problem": problem, "is_auth": is_auth}

    # Сделать рендер веб-страницы и отправить ответ
    return HttpResponse(template.render(contex, request))


def account(request):
    id = request.session["session_id"]
    user = User.objects.get(pk=id)
    message = "<h1>Account page</h1>"
    message += f"<h1>Login: {user.username} </h1>"
    message += f"<h1>Email: {user.email} </h1>"
    message += f"<h1>First Name: {user.first_name} </h1>"
    message += f"<h1>Last Name: {user.last_name} </h1>"
    return HttpResponse(message)
