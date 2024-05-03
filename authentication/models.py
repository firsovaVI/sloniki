from django.db import models
from prototype.models import Problem
# Create your models here.


# Добавить в view.detail добавление в solved_problem решенной проблемы по id
class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    GROUPS = {"ST": "Ученик", "TH": "Преподаватель"}
    group = models.CharField(max_length=2, choices=GROUPS, default="ST")

    solved_problems = models.ManyToManyField(Problem, null=True, blank=True )

    def __str__(self):
        return self.username
