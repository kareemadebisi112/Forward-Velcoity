from django.shortcuts import render
from .forms import LeadForm
import os
from dotenv import find_dotenv, load_dotenv
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import parse_data, get_current_year
from django.http import JsonResponse
from .services import make_lead


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
# Create your views here.


def index(request):
    services = Service.objects.all()
    from_email = os.getenv("EMAIL_HOST_USER")
    template = 'main/emails/email.html'
    form = LeadForm()

    context = {
        'form': form,
        'message': 'Thank you for contacting us!',
        'services': services,
        'hero': Hero.objects.first(),
        'about': About.objects.first(),
        'images': Image.objects.all(),
        'year': get_current_year()
    }
    return render(request, 'main/index.html', context)

def contact(request): 
    form = LeadForm()
    context =  {
        'form': form,
        'year': get_current_year()
    }
    return render(request, 'main/contact.html', context)

def email(request):
    return render(request, 'main/emails/email.html')

class EditPage(APIView):
    def put(self, request):
        # print(request.data)
        data = request.data
        print(data)
        update_hero, update_about = parse_data(data)

        hero = Hero.objects.get(id=update_hero['hero_id'])
        about = About.objects.get(id=update_about['about_id'])
        
        hero.title = update_hero['title']
        hero.description = update_hero['description']
        hero.button_text = update_hero['button_text']
        hero.save()

        about.title = update_about['title']
        about.description = update_about['description']
        about.highlight_text = update_about['highlight_text']
        about.year = update_about['year']
        about.mission_text = update_about['mission_text']
        about.vision_text = update_about['vision_text']
        about.values_text = update_about['values_text']
        about.save()

        return Response(status=status.HTTP_200_OK)
    

def post_lead(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        name = data['name']
        email = data['email']
        service = data['service']
        message = data['message']
        make_lead(name, email, service, message)
        first_name = name.split(' ')[0]
        return render(request, 'main/thankyou.html', {'name': first_name})
    return JsonResponse({'message': 'Error'}, status=400)