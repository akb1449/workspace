from django.shortcuts import render
from .models import Education, Experience

def home(request):
    """
    Renders resume app home page from templates
    """
    qs = Resume.objects.all()
    context = {'decks': qs}
    return render(request, 'resume/home.html', context)
