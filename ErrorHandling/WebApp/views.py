from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def error_404(request,exception):
    return render(request,'myapp/404.html')