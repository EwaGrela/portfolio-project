from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    title = "This is my homepage"
    jobs = Job.objects.all
    return render(request, 'jobs/home.html', {'title':title, 'jobs': jobs})