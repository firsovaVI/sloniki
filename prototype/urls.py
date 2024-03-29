from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:problem_id>/", views.detail, name="detail"),
    path("registration/", views.registration, name="registration"),
    path("authorization/", views.authorization, name="authorization"),
]
