from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
#from .models import Lecturer,Course,Classroom
from django.http import HttpResponse,HttpResponseRedirect
from .models import Testimonial, Facebook



@csrf_exempt
def home(request):
    context = {
        'message': Testimonial.objects.all(),
        'link': Facebook.objects.all()
        }

    return render(request, 'main/index.html', context)


@csrf_exempt
def about(request):
    return render(request, 'main/about.html')


@csrf_exempt
def clinics(request):
    return render(request, 'main/clinics.html')


@csrf_exempt
def social(request):
    return render(request, 'main/social.html')



@csrf_exempt
def contact(request):
    return render(request, 'main/contact.html')

def maredza(request):
    return render(request, 'main/maredza.html')


def kanyiwe(request):
    return render(request, 'main/kanyiwe.html')



def chipumha(request):
    return render(request, 'main/chipumha.html')



def forbes(request):
    return render(request, 'main/forbes.html')


def tavha(request):
    return render(request, 'main/tavha.html')
