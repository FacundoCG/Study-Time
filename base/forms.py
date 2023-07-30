from django import forms
from .models import Study

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class StudyForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    formal_study_hours = forms.DurationField()
    informal_study_hours = forms.DurationField()

    class Meta:
        model = Study
        fields = ["date", "formal_study_hours", "informal_study_hours"]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
                "autocomplete": "off",
            }
        ),
    )

    email = forms.CharField(
        label="Username",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
                "autocomplete": "off",
            }
        ),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].widget.attrs["autocomplete"] = "off"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["type"] = "password"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
