from django.db import models


class Problem(models.Model):
    headline = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    statement = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.headline
