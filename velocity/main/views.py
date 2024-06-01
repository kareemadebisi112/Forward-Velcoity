from django.shortcuts import render
from .forms import LeadForm
from django.core.mail import send_mail as send_email
import os
from dotenv import find_dotenv, load_dotenv
from django.template.loader import render_to_string
from django.utils.html import strip_tags

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Create your views here.


def index(request):
    from_email = os.getenv("EMAIL_HOST_USER")
    template = 'main/emails/email.html'
    form = LeadForm()

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()

            context = {
                'name': form.cleaned_data['name'].split(' ')[0],
            }

            convert_to_html_context = render_to_string(template, context)
            plain_message = strip_tags(convert_to_html_context)
            
            send_email(
                subject='New Lead',
                message=plain_message,
                from_email=from_email,
                recipient_list=[form.cleaned_data['email']],
                html_message=convert_to_html_context,
                fail_silently=False,
            )

            return render(request, 'main/index.html', {'form': form, 'message': 'Thank you for contacting us!'})

    return render(request, 'main/index.html', {'form': form})

def contact(request): 
    form = LeadForm()
    return render(request, 'main/contact.html', {'form': form})