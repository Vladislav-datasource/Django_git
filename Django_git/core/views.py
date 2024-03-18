from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import*


def home(request):
    return render(request, 'core/layout.html')


def data(request):
    return render(request, 'core/data.html')


def git_projects(request):
    return render(request, 'core/git_projects.html')


def add_user(request):
    error = ''
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form is invalid'

    form = PersonForm()
    form_methods = {
        'form': form,
        'error': error
    }

    return render(request, 'registration/profile.html', form_methods)