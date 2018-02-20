from django.shortcuts import render
from .models import Education, Experience

def home(request):
    """
    Renders resume app home page for the webpage portfolio "Andry Bintoro"
    Returns home.html page
    """
    qs_exp = Experience.objects.all()
    qs_edu = Education.objects.all()
    context = {'experience': qs_exp, 'education': qs_edu}
    #print(context)
    return render(request, 'resume/resume.html', context)
#
