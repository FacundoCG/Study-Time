from django import forms
from .models import Study

class StudyForm(forms.ModelForm):

    
    date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    formal_study_hours = forms.DurationField()
    informal_study_hours = forms.DurationField()

    class Meta:
        model = Study
        fields = ["date","formal_study_hours","informal_study_hours"]
       

        