#coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Group(TimeStampedModel):
    group = models.CharField(max_length=10,verbose_name=u'Название группы вопросов')


    def __unicode__(self):
        return self.group

Choices = (
    ('1', 'Первый'),
    ('2', 'Второй'),
    ('3', 'Третий'),
    ('4', 'Четвертый'),
    ('5', 'Пятый'),
)


class Question(TimeStampedModel):
    question = models.TextField(max_length=100, verbose_name=u'Текст вопроса')
    group = models.ForeignKey(Group)
    a1 =models.CharField(max_length=50, verbose_name=u'Первый ответ')
    a2 = models.CharField(max_length=50, verbose_name=u'Второй ответ')
    a3 = models.CharField(max_length=50, verbose_name=u'Третий ответ')
    a4 = models.CharField(max_length=50, verbose_name=u'Четвертый ответ', blank=True)
    a5 = models.CharField(max_length=50, verbose_name=u'Пятый ответ', blank=True)
    correct = models.CommaSeparatedIntegerField(max_length=10, choices=Choices, default='1')

    def __unicode__(self):
        return self.question