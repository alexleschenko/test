from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView, View
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
        q = models.Question.objects.filter(group_id=url_parametr)

        return q

class TestResult(View):
    template_name = 'result.html'

    def post(self, request):
        group_id = self.request.POST.get('group')
        answers = models.Question.objects.filter(group_id=group_id).values('id', 'correct')
        correct = 0
        for i in answers:
            user_answer = self.request.POST.get(str(i['id']))
            if user_answer == str(i['correct']):
                correct += 1
        user_response = "correct: {0}, total: {1}. Are you agree?".format(correct, models.Question.objects.filter(group_id=group_id).count())
        return HttpResponse(user_response)