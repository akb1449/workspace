from django.shortcuts import render

def home(request):
    '''
    Renders Home page
    '''
    return render(request, 'home.html')

def resume(request):
    '''
    Renders Resume page
    '''
    return render(request, 'resume.html')

def portfolio(request):
    '''
    Renders Portfolio page
    '''
    return render(request, 'portfolio.html')

def contact(request):
    '''
    Renders Contact page
    '''
    return render(request, 'contact.html')
