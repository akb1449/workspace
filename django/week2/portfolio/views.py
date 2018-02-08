from django.shortcuts import render

def home(request):
    """
    Takes the request and renders Home page
    """
    return render(request, 'home.html')

def resume(request):
    """
    Takes the request and renders Resume page
    """
    return render(request, 'resume.html')

def portfolio(request):
    """
    Takes the request and renders Portfolio page
    """
    return render(request, 'portfolio.html')

def contact(request):
    """
    Takes the request and renders Contact page
    """
    return render(request, 'contact.html')
