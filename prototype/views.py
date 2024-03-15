from django.http import HttpResponse
from django.template import loader

from .models import Problem


def index(request):
    problems_list = Problem.objects.all()
    template = loader.get_template("prototype/index.html")
    contex = {"problems_list": problems_list}
    return HttpResponse(template.render(contex, request))


def detail(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    status = None

    if request.method == "POST":
        if request.POST["user_answer"] == problem.answer:
            status = "Правильный ответ"
        else:
            status = "Неверный ответ"

    template = loader.get_template("prototype/detail.html")
    contex = {"problem": problem, "status": status}
    return HttpResponse(template.render(contex, request))
