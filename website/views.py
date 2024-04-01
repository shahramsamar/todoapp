from django.shortcuts import render
from django.http import HttpResponse
from website.models import BasicInformationModel, SkillModel
    


def index(request):
    BasicInfo = BasicInformationModel.objects.first()
    Skills = SkillModel.objects.all()
    context ={
        'BasicInfo':BasicInfo,
        'Skills': Skills
        }
    return render(request, "website/index.html", context)

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")
    
    