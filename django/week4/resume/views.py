from django.shortcuts import render
from .models import Resume, Education, Experience

def home(request):
    """
    Renders resume app home page for the webpage portfolio "Andry Bintoro"
    Returns resume.html page
    """
    my_resume = Resume.objects.first()

    context = { 'resume':my_resume, }
    #print(context)
    return render(request, 'resume/resume.html', context)
