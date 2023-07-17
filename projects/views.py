from django.shortcuts import render
from .models import project
from django.views import generic

# Create your views here.
def index(request):
    num_projects = project.objects.all().count()
    projects = project.objects.all()
    context = {
        'num_projects': num_projects,
        'projects': projects
    }
    return render(request, 'index.html', context=context)

class ProjectListView(generic.ListView):
    model = project
