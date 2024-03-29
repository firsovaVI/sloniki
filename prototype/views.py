from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Problem, User
from .forms import UserForm


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


def registration(request):
    status = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required:
            # create new user
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User(username=username, password=password)
            user.save()

            # redirect to a new URL: home page
            return HttpResponseRedirect(reverse("index"))
        else:
            status = True

    template = loader.get_template('prototype/registration.html')
    return HttpResponse(template.render({'status': status}, request))


def authorization(request):
    status = False

    if request.method == 'POST':
        status = True
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username__exact=username)
        except (KeyError, User.DoesNotExist):
            user = None

        if user:
            if user.password == password:
                # redirect to a new URL: home page
                return HttpResponseRedirect(reverse("index"))

    template = loader.get_template('prototype/authorization.html')
    return HttpResponse(template.render({'status': status}, request))
