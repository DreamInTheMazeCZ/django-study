# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    # return HttpResponse("Hello World!")
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymems' : mymembers,
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id_num):
    mymember = Member.objects.get(id=id_num)
    template = loader.get_template('details.html')
    context = {
        'mymem' : mymember,
    }
    
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymems = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mymems
    }
    return HttpResponse(template.render(context, request))