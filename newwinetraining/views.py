from django.shortcuts import render

def home(request):
    
    
    # Render the HTML template index.html
    return render(request, ‘index.html’, context=context)