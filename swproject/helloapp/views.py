from django.shortcuts import render
from .models import Search

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')

def search(request):
    if request.method=='POST':
        searched = request.POST['searched']        
        contents = Search.objects.filter(name__contains=searched)   #contents=혼잡도
        return render(request, 'searched.html', {'searched': searched, 'contents': contents})
    else:
        return render(request, 'searched.html', {})
