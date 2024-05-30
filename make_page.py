"""
    Used to make new pages in the Django project
    Usage: python make_page.py

    Enter a list of names (separated by commas): name1, name2, name3...
    This will create the following files:
    - name.html

    This will edit the following files:
    - views.py
    - urls.py
    - main.html

    The views.py file will have the following functions:
    - def name(request)

    The urls.py file will have the following path:
    - path('name/', views.name, name='name'),

    The main.html file will have the following block:
    - 

    The name.html file will have the following block:
    - {% extends 'main/main.html' %}
    - {% load static %}
    - {% block content %}
    - {% endblock content %}

    The name.html file will be created in the following directory:
    - {project}/main/templates/main/

    05/07/2024
"""
views = open("velocity/main/views.py", "a")
urls = open("velocity/main/urls.py", "a")
main_html = open("velocity/main/templates/main/main.html", "a")

# Create Page View
def create_page_view(name):
    views.write(f"\n\ndef {name}(request): \n return render(request, 'main/{name}.html')")

# Create URL Path
def create_url_path(name):
    urls.write(f"\n    path('{name}/', views.{name}, name='{name}'),")

# Create HTML Template
def create_html_template(name):
    new_html = open(f"velocity/main/templates/main/{name}.html", "a")
    html_line1 = "{% extends 'main/landing_main.html' %}"
    html_line2 = "{% load static %}"
    html_line3 = "{% block content %}"
    html_line4 = "{% endblock content %}"
    new_html.write(f"{html_line1}"
                     f"\n{html_line2}"
                    f"\n{html_line3}"
                    f"\n{html_line4}")


# Close Files
def close_files():
    views.close()
    urls.close()
    main_html.close()

if __name__ == "__main__":
    names = input("Enter a list of names (separated by commas): ").split(",")
    for name in names:
        create_page_view(name.strip())
        create_url_path(name.strip())
        create_html_template(name.strip())
    close_files()