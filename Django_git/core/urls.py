from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data', views.data, name='data'),
    path('git_projects', views.git_projects, name='git_projects')
]