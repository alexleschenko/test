from django.http import request
from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView
from django.views.generic.list import ListView

import models

class MainView(TemplateView):
    template_name = 'main.html'


class TestView(ListView):

    model = models.Group
    template_name = 'test.html'
    context_object_name = 'packs'

class QuestionView(ListView):
    template_name = 'test2.html'
    context_object_name = 'questions'

    def get_queryset(self):
        url_parametr = self.kwargs['group_id']
        return models.Question.objects.filter(group_id=url_parametr)
