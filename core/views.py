from django.shortcuts import render
from .models import RainbowColor


def index(request):
    # Get all rainbow colors using the class method
    colors = RainbowColor.get_all_colors()

    # Create a context dictionary with the colors
    context = {
        'colors': colors
    }

    # Render the template with the context data
    return render(request, 'index.html', context)
