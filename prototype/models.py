from django.db import models


class Problem(models.Model):
    headline = models.CharField(max_length=255)
    statement = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.headline


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username