from django.http import HttpResponse
from django.shortcuts import render
from .models import Stage, Exam
from django.contrib.auth.models import User
from career.models import Career

# Create your views here.
def create(request):
    stage = Stage.objects.get(pk=1)
    career = Career.objects.get(pk=1)
    user = User.objects.create(
            username = 'cuatro',
            password = 'cuatro'
        )
    exam = Exam.objects.create(user = user,
                               stage = stage,
                               career = career)
    exam.set_modules()
    exam.set_questions()
    return HttpResponse('Usuario y examen creado')
