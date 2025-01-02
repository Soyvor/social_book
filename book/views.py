from django.shortcuts import render
from django.http import HttpResponse

# Normal views
def register(request):
    return render(request, 'book/register.html')

def login(request):
    return render(request, 'book/login.html')

# Error views
def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/500.html', status=500)

def error_503(request):
    return render(request, 'errors/503.html', status=503)
