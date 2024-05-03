from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("account/", views.account, name="account"),
    path("<int:problem_id>/", views.detail, name="detail"),
    path("account/homework-<int:homework_id>/", views.homework, name="homework"),
    path("account/homework-<int:homework_id>/gradebook/", views.gradebook, name="gradebook"),
    path("api/user/", views.user_detail_api),
    path("api/user/all/", views.all_students_api),
    path("api/homework/<int:id>/", views.homework_detail_api),
    path("api/homework/all/", views.all_homeworks_api),
]
