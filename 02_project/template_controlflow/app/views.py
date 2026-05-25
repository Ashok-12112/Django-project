from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        "blogs": [
            {"title": "Django", "is_featured": True, "author": "ashok"},
            {"title": "python", "is_featured": False, "author": "litan"},
            {"title": "react", "is_featured": False, "author": "gunu"},
        ]
    }

    return render(request, 'data.html', context)