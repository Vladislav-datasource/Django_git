from django.shortcuts import render


def home(request):
    return render(request, 'core/layout.html')


def data(request):
    return render(request, 'core/data.html')


def git_projects(request):
    return render(request, 'core/git_projects.html')