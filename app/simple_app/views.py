from django.shortcuts import render

# Create your views here.

def index(request):
    '''index'''
    template_name= 'index.html'
    return render(request, template_name,{})

def bmi(request):
    '''bmi'''
    template_name='bmi.html'
    return render(request, template_name,{})