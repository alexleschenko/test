from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.list import ListView

import models

class MainView(TemplateView):
    template_name = 'main.html'


class TestView(ListView):

    def get(self, request):
        packs = models.Group.objects.filter()
        return render(request, 'test.html', {'packs':packs})

class QuestionView(TemplateView):
    pass
