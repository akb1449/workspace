from django.shortcuts import render
from .models import Resume, Education, Experience

def home(request):
    """
    Renders resume app home page for the webpage portfolio "Andry Bintoro"
    Returns resume.html page
    """
    my_resume = Resume.objects.first()
    full_name = Resume.objects.first().get_full_name()
    qs_exp = my_resume.get_experience()
    qs_edu = my_resume.get_education()

    context = { 'resume':my_resume,
                'name':full_name,
                'experience':qs_exp,
                'education':qs_edu }
    #print(context)
    return render(request, 'resume/resume.html', context)
