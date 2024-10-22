from django.shortcuts import render
from .forms import LeadForm
from django.core.mail import send_mail as send_email
import os
from dotenv import find_dotenv, load_dotenv
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import parse_data
from django.http import JsonResponse


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
# Create your views here.


def index(request):
    services = Service.objects.all()
    from_email = os.getenv("EMAIL_HOST_USER")
    template = 'main/emails/email.html'
    form = LeadForm()

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name'].split(' ')[0]
            context = {
                'form': form,
                'message': 'Thank you for contacting us!',
                'services': services,
                'hero': Hero.objects.first(),
                'about': About.objects.first(),
                'images': Image.objects.all()
            }

            convert_to_html_context = render_to_string(template, context)
            plain_message = strip_tags(convert_to_html_context)
            print('Name', name)
            
            # send_email(
            #     subject='New Lead',
            #     message=plain_message,
            #     from_email=from_email,
            #     recipient_list=[form.cleaned_data['email']],
            #     html_message=convert_to_html_context,
            #     fail_silently=False,
            # )
            return render(request, 'main/index.html', context)
    context = {
        'form': form,
        'message': 'Thank you for contacting us!',
        'services': services,
        'hero': Hero.objects.first(),
        'about': About.objects.first(),
        'images': Image.objects.all()
    }
    return render(request, 'main/index.html', context)

def contact(request): 
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact.html', {'form': form, 'message': 'Thank you for contacting us!'})
    return render(request, 'main/contact.html', {'form': form})

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