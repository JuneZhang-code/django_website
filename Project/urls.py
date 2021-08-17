from django.urls import path
from . import views

app_name = 'Project'

urlpatterns = [

    path('', views.all_projects, name='all_projects'),
    path('<int:Project_id>/', views.detail, name='detail'),



]
