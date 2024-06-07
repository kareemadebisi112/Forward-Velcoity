# Use for Create + Update
from .models import *

def make_lead(name, email, service, message):
    return Lead.objects.create(
        name=name, 
        email=email, 
        service=service, 
        message=message
    )

def make_service(name, description, icon, html_id):
    return Service.objects.create(
        name=name, 
        description=description, 
        icon=icon, 
        html_id=html_id
    )

def make_hero(title, description, button_text, button_link):
    return Hero.objects.create(
        title=title, 
        description=description, 
        button_text=button_text, 
        button_link=button_link
    )