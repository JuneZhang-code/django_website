from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def all_projects(request):
    Projects = Project.objects.order_by('-date')
    return render(request,'Project/all_projects.html',{'Projects':Projects})

def detail(request, Project_id):
    project = get_object_or_404(Project, pk=Project_id)
    return render(request, 'Project/detail.html',{'Project':project})
