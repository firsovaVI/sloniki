from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User


def registration(request):
    """Веб-сервис для регистрации аккаунта нового пользователя"""
    status = False

    # Если получена заполненная форма регистрации
    if request.method == "POST":

        # 1. Получить логин и пароль
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # 2. Провести валидацию данных

        # 3. Проверить уникальность логина

        # 4. Добавить пользователя в базу данных
        user = User(username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
        user.save()

        # 5. Создать пользовательскую сессию
        request.session["session_id"] = user.id

        # redirect to a new URL: home page
        return HttpResponseRedirect(reverse("index"))

    template = loader.get_template('registration.html')
    return HttpResponse(template.render({'status': status}, request))


def login(request):
    """Веб-сервис для аутентификации пользователя"""
    status = False

    # Если получена заполненная форма входа
    if request.method == 'POST':
        status = True

        # 1. Получить логин и пароль
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username__exact=username)
        except (KeyError, User.DoesNotExist):
            user = None

        # 3. Проверить существование пользователя с полученным логином
        if user:

            # 4. Проверить совпадение пароля
            if user.password == password:

                # 5. Создать пользовательскую сессию
                request.session["session_id"] = user.id

                # redirect to a new URL: home page
                return HttpResponseRedirect(reverse("index"))

    # Если получен запрос на получение пустой формы
    template = loader.get_template('login.html')
    return HttpResponse(template.render({'status': status}, request))


def logout(request):
    """Веб-сервис для выхода из аккаунта пользователя"""
    try:
        # Удалить сессию, если она есть
        del request.session["session_id"]
    except KeyError:
        pass
    return HttpResponseRedirect(reverse("index"))
