from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .forms import StudyForm
from .models import Study
from django.urls import reverse_lazy

# Create your views here.

class CreateStudyTime(CreateView):
    form_class = StudyForm
    model = Study
    template_name = 'base/createStudyTime.html'
    success_url = reverse_lazy('index')

class StudyList (ListView):
    model = Study
    context_object_name = 'study_list'
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['guia'] = []
        context['total'] = []

        if (len(context['study_list']))>7:
            n = len(context['study_list']) - 1
            i = 1
            for i in range(n-6,n+1):
                context['guia'].append(context['study_list'][i])

        context['guia'].reverse()
       
        return context

class HistoryList(ListView):
    model = Study
    context_object_name = 'study_list'
    template_name = 'base/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['study_list'].objects.all().order_by('date')

        return context

class DateUpdate (UpdateView):
    model = Study
    form_class = StudyForm
    template_name = 'base/updateRecord.html'
    success_url = reverse_lazy('index')

class AboutView(TemplateView):
    template_name = 'base/about.html'
