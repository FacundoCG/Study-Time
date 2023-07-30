from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    FormView,
    DeleteView,
)
from django.db.models.functions import ExtractMonth, ExtractYear

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import StudyForm, SignUpForm, LoginForm
from .models import Study


# An auxiliar function which removes duplicated elements
def removeDuplicates(l: list) -> list:
    new_list: list = []

    for e in l:
        if e not in new_list:
            new_list.append(e)

    return new_list


# Views
class SignUp(FormView):
    template_name = "base/signup.html"
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        return super(SignUp, self).get(*args, **kwargs)


class LoginUser(LoginView):
    template_name = "base/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")


class StudyList(ListView):
    model = Study
    context_object_name = "study_list"
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["study_list"] = context["study_list"].filter(user=self.request.user)
        context["last_times"] = []
        number_times = len(context["study_list"])

        if number_times > 7:
            context["last_times"] = context["study_list"][number_times - 7 :]
        else:
            context["last_times"] = context["study_list"]

        context["last_times"].reverse()

        return context


class HistoryList(ListView):
    model = Study
    context_object_name = "study_list"
    template_name = "base/history.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        month = self.request.GET.get("month", None)
        year = self.request.GET.get("year", None)

        if month:
            queryset = queryset.annotate(month=ExtractMonth("date")).filter(month=month)
        elif year:
            queryset = queryset.annotate(year=ExtractYear("date")).filter(year=year)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        unique_months = Study.objects.filter(user=self.request.user).dates(
            "date", "month", order="ASC"
        )
        context["months"] = [month.strftime("%B") for month in unique_months]
        context["months"] = removeDuplicates(context["months"])

        unique_years = Study.objects.filter(user=self.request.user).dates(
            "date", "year", order="ASC"
        )
        context["years"] = [year.year for year in unique_years]

        return context


class CreateStudyTime(CreateView):
    form_class = StudyForm
    model = Study
    template_name = "base/createStudyTime.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateStudyTime, self).form_valid(form)


class UpdateStudyTime(UpdateView):
    model = Study
    form_class = StudyForm
    template_name = "base/updateRecord.html"
    success_url = reverse_lazy("index")


class StudyDeleteView(DeleteView):
    model = Study
    success_url = reverse_lazy("index")


class AboutView(TemplateView):
    template_name = "base/about.html"
