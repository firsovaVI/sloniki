from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("account/", views.account, name="account"),
    path("<int:problem_id>/", views.detail, name="detail"),
]
