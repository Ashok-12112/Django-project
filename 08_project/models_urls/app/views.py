from django.shortcuts import render
from .models import Data_submit
from django.shortcuts import get_object_or_404

def home(request):
    data = Data_submit.objects.all()
    return render(request, 'home.html', {'data': data})

def userdata(request, user_id):
    user_data = get_object_or_404(Data_submit, pk=user_id) 
    return render(request, 'user_data.html', {'user_data': user_data})