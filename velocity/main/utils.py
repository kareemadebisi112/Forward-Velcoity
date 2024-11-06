from django.core.mail import send_mail
from datetime import datetime

def send_my_email(subject, message, from_email, recipient_list):
    return send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
    )

def parse_data(data):
    update_hero = {
        'title': data['data']['hero']['title'],
        'description': data['data']['hero']['description'],
        'button_text': data['data']['hero']['button'],
        'hero_id': data['data']['hero']['id']
    }
    update_about = {
        'title': data['data']['about']['title'],
        'description': data['data']['about']['description'],
        'highlight_text': data['data']['about']['highlight_text'],
        'year': data['data']['about']['year'],
        'mission_text': data['data']['about']['mission_text'],
        'vision_text': data['data']['about']['vision_text'],
        'values_text': data['data']['about']['values_text'],
        'about_id': data['data']['about']['id']
    }
    return update_hero, update_about

def get_current_year():
    return datetime.now().year