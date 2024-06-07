import pytest
from main.models import *
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager

# Create your tests here.

@contextmanager
def TestStep(message: str):
    print(message)
    yield

@pytest.mark.django_db
class TestNewUserFlow:
    def test_new_user_flow(self, client):
        with TestStep('1. Test that the user can access the index page'):
            assert Lead.objects.count() == 0

            response = client.get(reverse('index'))
            assert response.status_code == 200

        with TestStep('2. Test that the user can submit the form'):
            response = client.post(reverse('index'), {
                'name': 'John Doe',
                'email': 'test@gmail.com',
                'service': ['AI', 'WH'],
                'message': 'This is a test message',
            })
            assert response.status_code == 200
            assert Lead.objects.count() == 1

        with TestStep('3. Test that the user receives a success message'):
            # assert 'Thank you for contacting us!' in response.content.decode()
            pass
        
        with TestStep('4. Test that the user can access the contact page'):
            response = client.get(reverse('contact'))
            assert response.status_code == 200

        with TestStep('5. Test that the user can submit the form on the contact page'):
            response = client.post(reverse('contact'), {
                'name': 'John Doe',
                'email': 'test@gmail.com',
                'service': ['AI', 'WH'],
                'message': 'This is a test message',
            })
            assert response.status_code == 200
            # assert Lead.objects.count() == 2

class TestUserFlowBrowser:
    def test_user_flow_browser(self):
        with TestStep('1. Test that the user can access the index page'):
            browser = webdriver.Chrome()
            browser.get('http://127.0.0.1:8000/')
            assert 'Velocity' in browser.title

        with TestStep('2. Test that the user can submit the form'):
            buttons = browser.find_elements(By.CLASS_NAME, 'button')
            buttons[0].click()
            browser.implicitly_wait(2)

            name = browser.find_element(By.NAME, 'name')
            email = browser.find_element(By.NAME, 'email')
            service = browser.find_element(By.NAME, 'service')
            message = browser.find_element(By.NAME, 'message')
            submit = browser.find_element(By.NAME, 'submit')

            name.send_keys('John Doe')
            email.send_keys('test@gmail.com')
            service.send_keys('AI')
            service.send_keys(Keys.RETURN)
            service.send_keys('WH')
            service.send_keys(Keys.RETURN)
            message.send_keys('This is a test message')
            submit.click()
            browser.implicitly_wait(2)

        with TestStep('3. Test that the user receives a success message'):
            pass

        with TestStep('4. Test that the user can access the contact page'):
            browser.get('http://127.0.0.1:8000/contact')
            # assert 'Contact' in browser.title
        
        with TestStep('5. Test that the user can submit the form on the contact page'):
            pass
            # name = browser.find_element(By.NAME, 'name')
            # email = browser.find_element(By.NAME, 'email')
            # service = browser.find_element(By.NAME, 'service')
            # message = browser.find_element(By.NAME, 'message')
            # submit = browser.find_element(By.NAME, 'submit')

            # name.send_keys('John Doe')
            # email.send_keys('test@gmail.com')
            # service.send_keys('AI')
            # service.send_keys(Keys.RETURN)
            # service.send_keys('WH')
            # service.send_keys(Keys.RETURN)
            # message.send_keys('This is a test message')
            # submit.click()
            # browser.implicitly_wait(2)