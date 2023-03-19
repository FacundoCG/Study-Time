from django.urls import path
from .views import CreateStudyTime, StudyList, HistoryList, AboutView, DateUpdate

urlpatterns = [
    path('', StudyList.as_view(), name="index"),
    path('create/', CreateStudyTime.as_view(), name="create"),
    path('history/', HistoryList.as_view(), name="history"),
    path('aboutme/', AboutView.as_view(), name="about"),
    path('update-date/<int:pk>/', DateUpdate.as_view(), name="update"),
]