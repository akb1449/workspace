from django.shortcuts import render

def home(request):

    '''
    Renders home page
    '''
    #a dictionary with a keyword "our_greeting" mapping to the variable greeting defined above
    greeting = "uStudy - the best site in the world"
    #create a variable with the days of the week as a list
    days_of_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    #then add to context
    context = {'our_greeting':greeting, 'weekday_list':days_of_week}
    return render(request, 'home.html', context)
