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

def user_detail_api(request):
    """Endpoint, который возвращает личную информацию об авторизированном пользователе"""
    id = request.session["session_id"]
    user = User.objects.get(pk=id)
    
    data = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'group': user.group
        }
    return JsonResponse(data)

def all_students_api(request):
    """Endpoint, который возвращает список учеников в данном классе"""
    students = User.objects.filter(group='ST')
    
    data = []
    for student in students:
        solved_problems_list = []
        for p in student.solved_problems.all():
            solved_problems_list.append(p.pk)
        
            st = {
                'first_name': student.first_name,
                'last_name': student.last_name,
                'solved_problems': solved_problems_list
                }
            data.append(st)
    
    return JsonResponse({'students_list': data})

def all_homeworks_api(request):
    """Endpoint, который возвращает список всех проверочных работ для класса"""
    id = request.session["session_id"]
    user = User.objects.get(pk=id)
    
    homeworks = Homework.objects.all()
    data = []
    for homework in homeworks:
        hw = {
            'homework_id': homework.pk,
            'headline': homework.headline,
            'deadline': homework.deadline,
            'url': reverse('homework', kwargs={'homework_id': homework.id})
            }
        if user.group == 'TH':
            hw['url'] += 'gradebook/'
        data.append(hw)
    return JsonResponse({'homeworks_list': data})

def homework_detail_api(request, id):
    """Endpoint, который возвращает информацию о проверочной работе по id"""
    homework = Homework.objects.get(pk=id)
    problems_list = []
    for problem in homework.problems.all():
        url = reverse('detail', kwargs={'problem_id': problem.id})
        p = {
            'problem_id': problem.id,
            'headline': problem.headline,
            'url': url
            }
        problems_list.append(p)
    
    data = {
        'headline': homework.headline,
        'deadline': homework.deadline,
        'problems': problems_list
        }
    return JsonResponse(data)
