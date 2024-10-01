from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'myapp/index.html')


def loginPage(request):
    return render(request, 'registration/login.html')