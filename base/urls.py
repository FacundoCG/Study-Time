from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from .views import StudyList, SignUp, LoginUser, CreateStudyTime, HistoryList, AboutView, UpdateStudyTime, StudyDeleteView


urlpatterns = [
    path("", login_required(StudyList.as_view()), name="index"),
    path("sign-up/", SignUp.as_view(), name="sign-up"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", login_required(LogoutView.as_view(next_page="login")), name="logout"),
    path("create", login_required(CreateStudyTime.as_view()), name="create"),
    path("history", login_required(HistoryList.as_view()), name="history"),
    path("about", login_required(AboutView.as_view()), name="about"),
    path("update-date/<int:pk>/", login_required(UpdateStudyTime.as_view()), name="update"),
    path("update-date/<int:pk>/delete", login_required(StudyDeleteView.as_view()), name="delete"),
]
