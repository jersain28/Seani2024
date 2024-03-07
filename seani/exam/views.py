from django.http import HttpResponse
from django.shortcuts import render
from .models import Stage, Exam
from django.contrib.auth.models import User
from career.models import Career

from .forms import CandidateForm
# Create your views here.
def home(request):
    user = request.user
    return render(request, 'exam/home.html', {"user": user})

def create(request):
    if request.method == 'GET':
        form = CandidateForm()
        return render(request, 'exam/add_user.html', {"form": form})
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            career = form.cleaned_data['career']
            stage = form.cleaned_data['stage']
            user = User.objects.create_user(
                                        username = username,
                                        email = email, password = password)
            exam = Exam.objects.create(user = user,
                                stage = stage,
                                career = career)
            exam.set_modules()
            exam.set_questions()

            user.first_name = first_name
            user.last_name = last_name
            user.save()            
            
            return HttpResponse('Usuario y examen creado')

    
    
    