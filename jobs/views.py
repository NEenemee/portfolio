from django.shortcuts import render, get_object_or_404
from .models import Job, Education
from .models import Project

# Create your views here.
def jobs(request):
    jobs = Job.objects.all()
    education = Education.objects.all()
    return render(request,'jobs/portfolio.html', {'jobs':jobs,'education':education})

def detail(request,job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job_detail})

def home(request):
    Job.objects.all().order_by('EndDate')
    return render(request, 'jobs/home.html',{'home': home})

def projects(request):
    projects = Project.objects
    return render(request,'jobs/projects.html',{'projects':projects})